import os
import torch
import numpy as np
from PIL import Image
import time
import random

class ProcessAndSave:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING",),
                "remove_prompt": ("STRING",),
                "images": ("IMAGE",),
                "output_dir": ("STRING", {"default": "ComfyUI/output"}),
                "filename_prefix": ("STRING", {"default": "Image"}),
                "overwrite": (["enable", "disable"], {"default": "disable"}),
                "compression": ("INT", {"default": 4, "min": 0, "max": 9})
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("image_paths", "text_paths")
    FUNCTION = "process_and_save"
    OUTPUT_NODE = True
    CATEGORY = "Custom"

    def process_and_save(self, prompt, remove_prompt, images, output_dir, filename_prefix, overwrite, compression):
        # 处理提示词
        list_prom = [item.strip() for item in prompt.split(",")]
        list_rem_prom = [item.strip() for item in remove_prompt.split(",")]
        result = [item for item in list_prom if item not in list_rem_prom]
        processed_prompt = ",".join(result)
        print("Processed Prompt:", processed_prompt)

        # 创建输出目录
        os.makedirs(output_dir, exist_ok=True)

        # 转换 overwrite 为布尔值
        overwrite_bool = (overwrite == "enable")

        # 获取当前 UTC 时间戳
        utc_time = time.strftime("%Y%m%d%H%M%S", time.gmtime())

        # 遍历每个图像并保存
        result = []
        for idx, image in enumerate(images):
            # 生成唯一的文件名
            unique_suffix = f"{utc_time}_{random.randint(1000, 9999):04d}_{idx:04d}"
            img_path = os.path.join(output_dir, f"{filename_prefix}_{unique_suffix}.png")
            if not os.path.exists(img_path) or overwrite_bool:
                # 确保图像张量的形状是 (channels, height, width)
                if len(image.shape) == 3 and image.shape[-1] == 3:
                    # 如果通道在最后，将其转换为 (channels, height, width)
                    image = image.permute(2, 0, 1)
                elif len(image.shape) != 3 or image.shape[0] not in [1, 3]:
                    raise ValueError(f"Unsupported image shape: {image.shape}. Expected (3, height, width) or (1, height, width).")

                # 将 PyTorch 张量转换为 PIL 图像
                image = image.cpu().numpy()
                image = (image * 255).astype(np.uint8)
                img = Image.fromarray(image.transpose(1, 2, 0))  # 转换回 (height, width, channels)

                # 保存图像
                img.save(img_path, format="PNG", quality=100 - compression * 10)  # 调整压缩质量

                # 生成对应的TXT文件
                txt_path = os.path.splitext(img_path)[0] + ".txt"
                with open(txt_path, "w", encoding="utf-8") as f:
                    f.write(processed_prompt)  # 写入处理后的提示词

                result.append((img_path, txt_path))

        # 返回图像路径和文本路径
        image_paths = [img_path for img_path, _ in result]
        text_paths = [txt_path for _, txt_path in result]
        return (image_paths, text_paths)