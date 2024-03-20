from .CharacterMap import CharacterMap
from .Meta import Meta
class Font:
    def __init__(self, meta, name, characterMap, dataUri):
        self._meta = meta
        self._name = name
        self._characterMap = characterMap
        self._dataUri = dataUri

    @property
    def meta(self) -> 'Meta':
        return self._meta

    @meta.setter
    def meta(self, value: 'Meta'):
        self._meta = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def characterMap(self) -> 'CharacterMap':
        return self._characterMap

    @characterMap.setter
    def characterMap(self, value: 'CharacterMap'):
        self._characterMap = value

    @property
    def numberOfGlyphs(self) -> int:
        numberOfGlyphs = 0 if self._characterMap is None else len(self._characterMap)
        return numberOfGlyphs

    @property
    def dataUri(self) -> str:
        return self._dataUri

    @dataUri.setter
    def dataUri(self, value: str):
        self._dataUri = value

    def to_dict(self):
        meta = {} if self._meta is None else self.meta.to_dict()
        name = "" if self.name is None else self.name
        characterMap = {} if self.characterMap is None else self.characterMap
        dataUri = "" if self._dataUri is None else self._dataUri
        numberOfGlyphs = 0 if self._characterMap is None else len(self._characterMap)
        return {
            "meta": meta,
            "name": name,
            "characterMap": characterMap,
            "numberOfGlyphs": numberOfGlyphs,
            "dataUri": dataUri,
        }