#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        """
        class_dict = {}
        if cls is not None:
            for key, value in FileStorage.__objects.items():
                if isinstance(value, cls):
                    class_dict[key] = value
            return class_dict
        else:
        """
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
<<<<<<< HEAD
            FileStorage.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {key: obj.to_dict() for key, obj \
                in FileStorage.__objects.items()}
            """
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            """
            json.dump(temp, f)

    def delete(self, obj=None):
        """Delete obj from __object if it's inside - if obj=None do nothing"""
        if obj is not None:
            delete = None
            for key, value in FileStorage.__objects.items():
                if obj == value:
                    delete = key
                    break
            if delete is not None:
                del FileStorage.__objects[delete]

    def reload(self):
        """Loads storage dictionary from file"""
        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
<<<<<<< HEAD
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    cls_name = val["__class__"]
                    if cls_name in classes:
                        cls = classes[cls_name]
                        FileStorage.__objects[key] = cls(**val)
                    # self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
