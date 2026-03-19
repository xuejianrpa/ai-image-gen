# AI 图像生成器插件

使用魔搭 ModelScope 的通义万相模型生成高质量 AI 图像。

## 安装

在 Claude Code 中运行以下命令：

```bash
/plugin install https://github.com/xuejianrpa/ai-image-gen
```

## 使用方法

### 方式一：直接描述想要的图片

只需用自然语言描述你想要的图片，Claude 会自动识别并调用此技能：

- "画一张图，一只可爱的猫咪坐在月亮上"
- "生成一张日落山景的图片"
- "帮我画一个未来城市"
- "Generate an image of a sunset over mountains"

### 方式二：使用斜杠命令

```
/ai-image-gen:ai-image-gen <图片描述>
```

## 前置条件

### 1. 配置 API Key

需要设置 ModelScope API Key 环境变量：

```bash
# macOS / Linux
export MODELSCOPE_API_KEY='your-modelscope-api-key'

# Windows (CMD)
set MODELSCOPE_API_KEY=your-modelscope-api-key

# Windows (PowerShell)
$env:MODELSCOPE_API_KEY='your-modelscope-api-key'
```

获取 API Key：[ModelScope 平台](https://modelscope.cn/)

### 2. 安装 Python 依赖

```bash
pip install requests Pillow
```

## 可用模型

| 模型 ID | 说明 |
|---------|------|
| `Tongyi-MAI/Z-Image-Turbo` | 快速生成（默认） |
| `Tongyi-MAI/Z-Image` | 更高质量，速度较慢 |

## 使用技巧

1. **描述具体**：比如 "一只金毛犬在秋天的落叶中玩耍" 比 "一只狗" 效果更好
2. **添加风格**：可以指定风格，如 "宫崎骏风格"、"照片级真实"、"油画风格"
3. **包含细节**：描述光线、氛围、构图、颜色等细节
4. **使用英文**：模型对英文提示词效果更好，Claude 会自动帮你翻译优化

## 示例

**用户输入：**
> 帮我画一只在月亮上的猫

**Claude 会：**
1. 优化提示词为英文
2. 调用生成脚本
3. 显示生成的图片
4. 询问是否需要调整

## 作者

**雪见** 📍 四川成都

- 微信：`soraaigc`（欢迎链接）
- 公众号：**雪见AI编程**（欢迎关注）

### 推荐链接

| 平台 | 链接 | 说明 |
|------|------|------|
| 知识星球 | https://t.zsxq.com/mC8bP | ⭐ **限时免费** 加入 |
| AI编程平台 | https://aigocode.com/invite/JHK8VZAQ | 🚀 AI编程 + OpenClaw 必备 |
| 飞书文档 | https://my.feishu.cn/wiki/XkNawOgzjiK4zektG6dcD4zXnxd | 📚 录播视频 + 文档教程 |

## 许可证

MIT License
