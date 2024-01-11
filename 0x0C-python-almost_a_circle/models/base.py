#!/usr/bin/python3
"""
The Base module
"""


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
