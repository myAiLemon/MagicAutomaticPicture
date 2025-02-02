import torch
import random

class MagicLatent:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "width": ("INT", {"default": 512, "min": 64, "max": 4096, "step": 8, "tooltip": "Width of the latent image"}),
                "height": ("INT", {"default": 512, "min": 64, "max": 4096, "step": 8, "tooltip": "Height of the latent image"}),
                "batch_size": ("INT", {"default": 1, "min": 1, "max": 64, "tooltip": "Batch size for the latent image"}),
            }
        }

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "generate"
    OUTPUT_NODE = True
    CATEGORY = "Custom"

    def generate(self, width, height, batch_size):
        # 生成一个随机数
        random_number = random.randint(0, 1)
        if random_number == 1:
            # 创建一个随机的 latent 张量
            latent = torch.rand((batch_size, 4, height // 8, width // 8), dtype=torch.float32)
        else:
            latent = torch.zeros((batch_size, 4, width // 8, height // 8), dtype=torch.float32)
        # 返回 latent 张量
        return ({"samples": latent},)