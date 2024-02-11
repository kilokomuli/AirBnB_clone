#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
"""Defines class FileStorage"""


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file
    to instances"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Creates instance of FIleStorage"""
        pass

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        Args:
            obj: object"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def serialize_user(self, user):
        """Serializes a User instance into dictionary format"""
        user_dict = user.to_dict()
        return user_dict

    def deserialize_user(self, user_dict):
        """Deserializes a dictionary into a User instance"""
        user_instance = User(**user_dict)
        return user_instance

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        serialized_obj = {}
        for key, value in FileStorage.__objects.items():
            if isinnstance(value, User):
                serialized_obj[key] = self.serialize_user(value)
            else:
                serialized_obj[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w', encoding="utf8") as file:
            json.dump(serialized_obj, file)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as myFile:
                my_obj_dump = myFile.read()
        except FileNotFoundError:
            return
        objects = json.loads(my_obj_dump)
        for key, value in objects.items():
            class_name = value.get('__class__')
            if class_name == 'User':
                objects[key] = self.deserialize_user(value)
            else:
                module = getattr(models, class_name, None)
                if module:
                    objects[key] = module(**value)
        self.__objects = objects
