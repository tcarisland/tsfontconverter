from dataclasses import dataclass
from py_ts_interfaces import Interface


@dataclass
class Glyph(Interface):
    glyphId: str = ""
    unicode: str = ""
