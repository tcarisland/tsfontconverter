class Glyph:
    def __init__(self, glyphId, unicode):
        self.glyphId = glyphId
        self.unicode = unicode

    @property
    def glyphId(self) -> int:
        return self._glyphId

    @glyphId.setter
    def glyphId(self, value: int):
        self._glyphId = value

    @property
    def unicode(self) -> str:
        return self._unicode

    @unicode.setter
    def unicode(self, value: str):
        self._unicode = value

    def to_dict(self):
        glyphId = "" if self._glyphId is None else self._glyphId
        unicode = "" if self._unicode is None else self._unicode
        return {
            "glyphId": glyphId,
            "unicode": unicode
        }