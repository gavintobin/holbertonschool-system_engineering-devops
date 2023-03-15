#!/usr/bin/python3
"""base model class"""
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, id, created_at, updated_at):
        self.id = str(uuid.uuid4)
        self.created_at = created_at
        self.updated_at = updated_at
        now = datetime.now

    @property
    def created_at(self):
        return self.created_at

    @created_at.getter
    def created_at(self, now):
        now = datetime.now = datetime.isoformat()
        return now

    @property
    def updated_at(self):
        return self.updated_at

    @updated_at.getter
    def updated_at(self):
        self.updated_at = datetime.now

    def __str__(self):
        strect = "[{}]".format(self.__name__)
        strect += "({})".format(self.id)
        strect += "{}".format(self.__dict__)

    def save(self):
        self.created_at = datetime.now
        self.updated_at = datetime.now
    def to_dict(self):
        mydict = self.__dict__
        mydict["__class__"] = 

