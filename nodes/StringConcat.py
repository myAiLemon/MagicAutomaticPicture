class StringConcat:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string1": ("STRING", {"default": "Magic✨", "multiline": False}),
                "string2": ("STRING", {"default": "GitHub_myAilemon", "multiline": False}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "concatenate"
    OUTPUT_NODE = True
    CATEGORY = "Custom"

    def concatenate(self, string1, string2):
        # 将两个字符串相加
        result = string1 + string2
        # 返回结果
        return result
