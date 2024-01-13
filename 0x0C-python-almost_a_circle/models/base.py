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
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        with open(f"{cls.__name__}.json", mode="a", encoding="utf-8") as fd:
            if list_objs is None:
                fd.write("[]")
            else:
                fd.write("[")
                for index, obj in enumerate(list_objs):
                    fd.write(cls.to_json_string(obj.to_dictionary()))
                    if index < len(list_objs) - 1:
                        fd.write(", ")
                fd.write("]")
