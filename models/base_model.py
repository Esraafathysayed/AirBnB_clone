#!/usr/bin/env python3
"""BaseModel class definition"""
import json
import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Constructor method"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, val in kwargs.items():
                if key == "id":
                    self.id = val
                    continue
                if key == "created_at":
                    self.created_at = datetime.fromisoformat(val)
                    continue
                if key == "updated_at":
                    self.updated_at = datetime.fromisoformat(val)
                    continue
                if key != "__class__":
                    setattr(self, key, val)
        else:
            models.storage.new(self)

    def __str__(self):
        """
        Return str representation of BaseModel instance
        """
        str = "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
        return str

    def save(self):
        """
        Save the instance to a file
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of the instance
        """
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic
