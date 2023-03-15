#!/usr/bin/python3
"""base model class"""
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4)
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        strect = "[{}]".format(self.__class__)
        strect += "({})".format(self.id)
        strect += "{}".format(self.__dict__)
        return strect

    def save(self):
        self.updated_at = datetime.utcnow()

    def to_dict(self):

        mydict = self.__dict__
        mydict["__class__"] = self.__class__
        mydict["created_at"] = self.created_at.isoformat()
        mydict["updated_at"] = self.updated_at.isoformat()
        return mydict