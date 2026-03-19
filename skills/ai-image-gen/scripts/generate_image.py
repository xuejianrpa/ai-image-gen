#!/usr/bin/env python3
"""
AI Image Generator using ModelScope API (Tongyi Wanxiang)
Usage: python generate_image.py "your prompt" [--output output_path.jpg] [--model model_id]
"""

import requests
import time
import json
import os
import sys
from pathlib import Path

# Configuration
BASE_URL = 'https://api-inference.modelscope.cn/'
DEFAULT_MODEL = 'Tongyi-MAI/Z-Image-Turbo'

def get_api_key():
    """Get API key from environment variable or prompt user."""
    api_key = os.environ.get('MODELSCOPE_API_KEY')
    if not api_key:
        print("Error: MODELSCOPE_API_KEY environment variable not set.")
        print("Please set it with: export MODELSCOPE_API_KEY='your-api-key'")
        sys.exit(1)
    return api_key

def generate_image(prompt: str, output_path: str = None, model: str = None) -> str:
    """
    Generate an image using ModelScope API.

    Args:
        prompt: Text description of the image to generate
        output_path: Path to save the generated image (default: ./generated_image.jpg)
        model: Model ID to use (default: Tongyi-MAI/Z-Image-Turbo)

    Returns:
        Path to the saved image file
    """
    api_key = get_api_key()
    model = model or DEFAULT_MODEL
    output_path = output_path or 'generated_image.jpg'

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "X-ModelScope-Async-Mode": "true"
    }

    # Submit image generation task
    print(f"Submitting image generation request...")
    print(f"  Model: {model}")
    print(f"  Prompt: {prompt}")

    response = requests.post(
        f"{BASE_URL}v1/images/generations",
        headers=headers,
        data=json.dumps({
            "model": model,
            "prompt": prompt
        }, ensure_ascii=False).encode('utf-8')
    )

    if response.status_code != 200:
        print(f"Error: API request failed with status {response.status_code}")
        print(f"Response: {response.text}")
        sys.exit(1)

    task_id = response.json().get("task_id")
    if not task_id:
        print(f"Error: No task_id in response: {response.json()}")
        sys.exit(1)

    print(f"Task submitted. Task ID: {task_id}")
    print("Waiting for image generation to complete...")

    # Poll for task completion
    poll_headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "X-ModelScope-Task-Type": "image_generation"
    }

    max_attempts = 60  # 5 minutes max wait time
    attempt = 0

    while attempt < max_attempts:
        attempt += 1

        result = requests.get(
            f"{BASE_URL}v1/tasks/{task_id}",
            headers=poll_headers
        )

        if result.status_code != 200:
            print(f"Warning: Poll request failed with status {result.status_code}")
            time.sleep(5)
            continue

        data = result.json()
        status = data.get("task_status")

        if status == "SUCCEED":
            image_url = data.get("output_images", [None])[0]
            if not image_url:
                print("Error: No image URL in response")
                sys.exit(1)

            # Download and save the image
            print(f"Downloading generated image...")
            img_response = requests.get(image_url)
            if img_response.status_code != 200:
                print(f"Error: Failed to download image, status {img_response.status_code}")
                sys.exit(1)

            # Ensure output directory exists
            output_dir = os.path.dirname(output_path)
            if output_dir:
                os.makedirs(output_dir, exist_ok=True)

            with open(output_path, 'wb') as f:
                f.write(img_response.content)

            print(f"Success! Image saved to: {output_path}")
            return output_path

        elif status == "FAILED":
            error_msg = data.get("message", "Unknown error")
            print(f"Error: Image generation failed - {error_msg}")
            sys.exit(1)

        # Still processing
        print(f"  Status: {status} (attempt {attempt}/{max_attempts})")
        time.sleep(5)

    print("Error: Timeout waiting for image generation")
    sys.exit(1)

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Generate AI images using ModelScope API (Tongyi Wanxiang)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python generate_image.py "A golden cat sitting on a throne"
  python generate_image.py "A sunset over mountains" --output sunset.jpg
  python generate_image.py "A cyberpunk city" --model Tongyi-MAI/Z-Image
        '''
    )

    parser.add_argument('prompt', help='Text description of the image to generate')
    parser.add_argument('--output', '-o', default='generated_image.jpg',
                        help='Output file path (default: generated_image.jpg)')
    parser.add_argument('--model', '-m', default=DEFAULT_MODEL,
                        help=f'Model ID to use (default: {DEFAULT_MODEL})')

    args = parser.parse_args()

    generate_image(args.prompt, args.output, args.model)

if __name__ == '__main__':
    main()
