#!/usr/bin/python3
"""
The Base module
"""
import json
from os import path


class Base:
    """
    THe Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        The initailize method

        (Args):
            id: This class will be the “base” of all other classes in
            this project.The goal of it is to manage id attribute in all
            your future classes and to avoid duplicating the same code
            (by extension, same bugs)
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is not None:
            list_objs = [ob.to_dictionary() for ob in list_objs]
        with open(f"{cls.__name__}.json", mode="w", encoding="utf-8") as fd:
            fd.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            obj = cls(1, 1)
        elif cls is Square:
            obj = cls(1)
        else:
            return None
        obj.update(**dictionary)
        return obj

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances:"""
        file_name = f"{cls.__name__}.json"
        if not path.isfile(file_name):
            return []
        with open(file_name, mode="r", encoding="utf-8") as fd:
            return [cls.create(**obj) for obj in cls.from_json_string(fd.read())]
        
