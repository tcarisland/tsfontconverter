class CharacterMap:
    def __init__(self, glyphs):
        self._glyphs = glyphs

    @property
    def glyphs(self) -> list:
        return self._glyphs

    @glyphs.setter
    def glyphs(self, value: list):
        self._glyphs = value