from .nodes.Magic_Prompt import IntegratedCLIPTextEncodeWithExtract
from .nodes.Magic_ProcessAndSave import ProcessAndSave
from .nodes.Magic_String import EditableStringNode
from .nodes.StringConcat import StringConcat


NODE_CLASS_MAPPINGS = {
    "IntegratedCLIPTextEncodeWithExtract": IntegratedCLIPTextEncodeWithExtract,
    "ProcessAndSave": ProcessAndSave,
    "EditableStringNode": EditableStringNode,
    "StringConcat": StringConcat,
}


NODE_DISPLAY_NAME_MAPPINGS = {
    "IntegratedCLIPTextEncodeWithExtract": "Magic✨ Integrated CLIP Text Encode With Extract",
    "ProcessAndSave": "Magic✨ Process and Save",
    "EditableStringNode": "Magic✨ Editable String Node",
    "StringConcat": "Magic✨ String Concatenation"
}
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
