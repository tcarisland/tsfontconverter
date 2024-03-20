import json
import re
from types import FunctionType

from ..fontmodel.Font import Font
def getFontDefinition():
    return reflect_class_to_json(Font)

def getGlyphDeginition():
    return ""

def getCharacterMapDefinition():
    return ""

def getMetaDefinition():
    return ""

def getTypeNameFromPropType(value):
    class_pattern = r"<class '((.*?\.)*)(.*?)'>"
    plain_class_pattern = r"<class '(.*?)'>"
    match = re.match(class_pattern, value)
    if match:
        return match.group(3)
    else:
        match = re.match(plain_class_pattern, value)
        if match:
            return match.group(1)
        else:
            return value

def reflect_class_to_json(class_def):
    properties = {}
    for name, attr in class_def.__dict__.items():
        if isinstance(attr, property):
            prop_type = attr.fget.__annotations__.get('return', 'unknown')
            properties[name] = prop_type
            value = getTypeNameFromPropType(str(prop_type))
            print("{k}: {v}".format(k=name, v=value))
    return ""

print(getFontDefinition())