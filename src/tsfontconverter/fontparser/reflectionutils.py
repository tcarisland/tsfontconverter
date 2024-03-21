import inspect
import json

from ..fontmodel.CharacterMap import CharacterMap
from ..fontmodel.Font import Font

from ..fontmodel.Glyph import Glyph
from ..fontmodel.Meta import Meta


def getClassDefinition(clazz):
    fontClassDefinition = inspect.signature(clazz.__init__)
    fontDict = {}
    for param_name, param in fontClassDefinition.parameters.items():
        if param_name is not "self":
            fontDict[param_name] = param.annotation.__name__
    return f"export interface {clazz.__name__} {json.dumps(fontDict, indent=1)}"

def getAllDefinitions():
    return [getClassDefinition(cls) for cls in [Glyph, CharacterMap, Meta, Font]]

