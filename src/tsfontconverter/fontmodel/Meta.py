class Meta:
    def __init__(self, designerUrl, licenseUrl, manufacturerUrl, description, sampleText):
        self.designerUrl = designerUrl
        self.licenseUrl = licenseUrl
        self.manufacturerUrl = manufacturerUrl
        self.description = description
        self.sampleText = sampleText

    @property
    def designerUrl(self) -> str:
        return self._designerUrl

    @designerUrl.setter
    def designerUrl(self, value: str):
        self._designerUrl = value

    @property
    def licenseUrl(self) -> str:
        return self._licenseUrl

    @licenseUrl.setter
    def licenseUrl(self, value: str):
        self._licenseUrl = value

    @property
    def manufacturerUrl(self) -> str:
        return self._manufacturerUrl

    @manufacturerUrl.setter
    def manufacturerUrl(self, value: str):
        self._manufacturerUrl = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str):
        self._description = value

    @property
    def sampleText(self) -> str:
        return self._sampleText

    @sampleText.setter
    def sampleText(self, value: str):
        self._sampleText = value

    def to_dict(self):
        description = "" if self._description is None else self._description
        license_url = "" if self._licenseUrl is None else self._licenseUrl
        designer_url = "" if self._designerUrl is None else self._designerUrl
        manufacturer_url = "" if self._manufacturerUrl is None else self._manufacturerUrl
        sample_text = "" if self._sampleText is None else self._sampleText
        return {
            "description": description,
            "licenseUrl": license_url,
            "designerUrl": designer_url,
            "manufacturerUrl": manufacturer_url,
            "sampleText": sample_text
        }