from .abstract_model import AbstractModel
from database.db import db


# Req. 1
class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data):
        super().__init__(data)

    # Req. 2
    def to_dict(self):
        return {
            "name": self.data.get("name"),
            "acronym": self.data.get("acronym")
        }

    # Req. 3
    @classmethod
    def list_dicts(cls):
        list_languages = []
        languages = cls._collection.find({})
        for language in languages:
            list_languages.append(cls(language).to_dict())
        return list_languages
