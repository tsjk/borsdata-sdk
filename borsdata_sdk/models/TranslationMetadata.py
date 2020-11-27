class TranslationMetadata:
    translationKey: str
    nameSv: str
    nameEn: str

    def __init__(self, nameSv, nameEn, translationKey):
        self.translationKey = translationKey
        self.nameSv = nameSv
        self.nameEn = nameEn
