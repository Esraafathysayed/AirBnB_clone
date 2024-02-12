#!/usr/bin/env python3
""" FileStorage """

import json
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

from models.base_model import BaseModel
import os


class FileStorage:
    """Class FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return Data"""
        return self.__objects

    def new(self, obj):
        """save in .__object"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """saving in json"""
        with open(self.__file_path, "w") as f:
            data = {}
            for k, v in self.__objects.items():
                data[k] = v.to_dict()
            if len(data) != 0:
                json.dump(data, f, indent=4)

    def reload(self):
        """reload json file to the endpoint"""
        classes = {"User": User, "State": State, "BaseModel": BaseModel,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review}

        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                restored = json.load(f)
                for k, v in restored.items():
                    if '__class__' in v:
                        cls = classes[v['__class__']]
                        obj = cls(**v)
                        self.__objects[k] = obj
