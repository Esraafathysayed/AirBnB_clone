#!/usr/bin/env python3
"""
FileStorage class definition to return a string value
"""
import json
from models.base_model import BaseModel
import os


class FileStorage:
    """FileStorage class for saving instances file json and objects"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all stored data returned the object"""
        return self.__objects

    def new(self, obj):
        """save instance in .__object string value object"""
        key_for_dic = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key_for_dic] = obj

    def save(self):
        """Save instance in __objects dictionary"""
        with open(self.__file_path, "w") as f:
            data = {}
            for k, v in self.__objects.items():
                data[k] = v.to_dict()
            if len(data) != 0:
                json.dump(data, f, indent=4)

    def reload(self):
        """Reload data from .json file"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                restor = json.load(f)
                for k, v in restor.items():
                    if '__class__' in v:
                        cls = v['__class__']
                        obj = cls(**v)
                        self.__objects[k] = obj
