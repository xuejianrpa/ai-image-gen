# AI Image Generator Plugin

[中文](README_CN.md) | English

Generate high-quality AI images using ModelScope's Tongyi Wanxiang (通义万相) model.

## Installation

Run the following command in Claude Code:

```bash
/plugin install https://github.com/xuejianrpa/ai-image-gen
```

## Usage

### Method 1: Natural Language

Simply describe the image you want, and Claude will automatically recognize and invoke this skill:

- "画一张图，一只可爱的猫咪坐在月亮上"
- "生成一张日落山景的图片"
- "Generate an image of a sunset over mountains"
- "Draw me a futuristic city"

### Method 2: Slash Command

```
/ai-image-gen:ai-image-gen <image description>
```

## Prerequisites

### 1. Configure API Key

Set the ModelScope API Key environment variable:

```bash
# macOS / Linux
export MODELSCOPE_API_KEY='your-modelscope-api-key'

# Windows (CMD)
set MODELSCOPE_API_KEY=your-modelscope-api-key

# Windows (PowerShell)
$env:MODELSCOPE_API_KEY='your-modelscope-api-key'
```

Get your API Key from [ModelScope](https://modelscope.cn/)

### 2. Install Python Dependencies

```bash
pip install requests Pillow
```

## Available Models

| Model ID | Description |
|----------|-------------|
| `Tongyi-MAI/Z-Image-Turbo` | Fast generation (default) |
| `Tongyi-MAI/Z-Image` | Higher quality, slower |

## Tips for Better Results

1. **Be specific**: "A golden retriever puppy playing in autumn leaves" is better than "a dog"
2. **Add style**: Specify style like "Studio Ghibli style", "photorealistic", "oil painting"
3. **Include details**: Describe lighting, mood, composition, colors
4. **Use English**: The model works better with English prompts; Claude will help translate and optimize

## Example

**User input:**
> 帮我画一只在月亮上的猫

**Claude will:**
1. Optimize the prompt to English
2. Call the generation script
3. Display the generated image
4. Ask if adjustments are needed

## Author

**雪见 (Xuejian)** 📍 Chengdu, Sichuan

- WeChat: `soraaigc`
- Official Account: **雪见AI编程**

### Recommended Links

| Platform | Link | Description |
|----------|------|-------------|
| Knowledge Planet | https://t.zsxq.com/mC8bP | ⭐ **Free to join** |
| AI Coding Platform | https://aigocode.com/invite/JHK8VZAQ | 🚀 AI Coding + OpenClaw |
| Feishu Docs | https://my.feishu.cn/wiki/XkNawOgzjiK4zektG6dcD4zXnxd | 📚 Video tutorials |

## Connect with Me

<p align="center">
  <img src="assets/wechat.jpg" width="200" alt="WeChat QR Code" />
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="assets/group.jpg" width="200" alt="AI Group QR Code" />
</p>

<p align="center">
  <b>Add WeChat</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>Join AI Group</b>
</p>

## License

MIT License
