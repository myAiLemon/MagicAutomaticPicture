from comfy.comfy_types import ComfyNodeABC  

class EditableStringNode(ComfyNodeABC):  
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
            } 
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "func"
    CATEGORY = "Custom Nodes/Text"

    def func(self, text):
        return (text,)