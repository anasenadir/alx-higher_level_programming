#!/usr/bin/python3
"""
The Base module
"""
import json


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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is not None:
            list_objs = [ob.to_dictionary() for ob in list_objs]
        with open(f"{cls.__name__}.json", mode="w", encoding="utf-8") as fd:
            fd.write(cls.to_json_string(list_objs))
