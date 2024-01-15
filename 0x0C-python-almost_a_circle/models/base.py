#!/usr/bin/python3
"""
The Base module
"""
import json
from os import path
import csv

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
            return [cls.create(**obj)
                    for obj in cls.from_json_string(fd.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes and deserializes in CSV"""
        filename = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            list_dic = [0, 0, 0, 0, 0]
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_dic = ['0', '0', '0', '0']
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for kv in range(len(list_keys)):
                    list_dic[kv] = obj.to_dictionary()[list_keys[kv]]
                matrix.append(list_dic[:])

        with open(filename, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(matrix)
    
    @classmethod
    def load_from_file_csv(cls):
        """lood from csv file
        """
        filename = "{}.csv".format(cls.__name__)

        if path.exists(filename) is False:
            return []

        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            csv_list = list(reader)

        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        for csv_elem in csv_list:
            dict_csv = {}
            for kv in enumerate(csv_elem):
                dict_csv[list_keys[kv[0]]] = int(kv[1])
            matrix.append(dict_csv)

        list_ins = []

        for index in range(len(matrix)):
            list_ins.append(cls.create(**matrix[index]))

        return list_ins
