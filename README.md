# AI Image Generator Plugin

Generate high-quality AI images using ModelScope's Tongyi Wanxiang (通义万相) model.

## Installation

```bash
/plugin install <your-github-repo-url>
```

## Usage

Use the skill by typing:
```
/ai-image-gen:ai-image-gen
```

Or simply describe what image you want:
- "画一张图，一只可爱的猫咪"
- "Generate an image of a sunset over mountains"
- "Draw me a futuristic city"

## Prerequisites

### Required environment variable:
```bash
export MODELSCOPE_API_KEY='your-modelscope-api-key'
```

Get your API key from [ModelScope](https://modelscope.cn/).

### Required Python packages:
```bash
pip install requests Pillow
```

## Available models

| Model ID | Description |
|----------|-------------|
| `Tongyi-MAI/Z-Image-Turbo` | Fast generation (default) |
| `Tongyi-MAI/Z-Image` | Higher quality, slower |

## Author

**雪见**
- WeChat: `soraaigc`
- 公众号: **雪见AI编程**

## License

MIT
