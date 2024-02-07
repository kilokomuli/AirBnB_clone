#!/usr/bin/python3
from datetime import datetime
import uuid
import models
"Defines class BaseModel"


class BaseModel:
    def __init__(self):
        """initializes class BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """string representation of the object"""
        str_ = "["
        str_ += str(self.__class__.__name__) + '] ('
        str_ += str(self.id) + ') ' + str(self.__dict__)
        return str_

    def save(self):
        """updates currrent instance attribute with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Dictionary representation of the object"""
        dict_obj = self.__dict__.copy()
        dict_obj['__class__'] = self.__class__.__name__
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()
        return dict_obj