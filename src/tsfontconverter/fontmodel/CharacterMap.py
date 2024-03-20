from typing import List

from .Glyph import Glyph


class CharacterMap:
    def __init__(self):
        self._glyphs = []

    @property
    def glyphs(self) -> List[Glyph]:
        return self._glyphs

    @glyphs.setter
    def glyphs(self, value: List[Glyph]):
        self._glyphs = value

    def to_dict(self):
        glyphs = [] if self._glyphs is None else [glyph.to_dict() for glyph in self._glyphs]
        return {
            "glyphs": glyphs
        }