from comfy.sd import CLIP
from nodes import CLIPTextEncode

class IntegratedCLIPTextEncodeWithExtract(CLIPTextEncode):
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "clip": ("CLIP", ),
                "text": ("STRING", {"multiline": True, "dynamicPrompts": True}),
            }
        }

    RETURN_TYPES = ("CONDITIONING", "STRING")  # 同时输出两种类型
    RETURN_NAMES = ("CONDITIONING", "prompt_text")  # 定义输出端口名称
    FUNCTION = "encode_with_extract"

    CATEGORY = "Custom Nodes/Integrated"

    def encode_with_extract(self, clip: CLIP, text: str):
        # 生成原始 CONDITIONING
        conditioning = super().encode(clip, text)[0]
        
        # 直接返回 CONDITIONING + 原始文本
        return (conditioning, text)