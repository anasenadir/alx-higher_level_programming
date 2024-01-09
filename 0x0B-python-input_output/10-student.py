#!/usr/bin/python3
"""
Class Module
"""


class Student:
    """
    Student Class
    """
    def __init__(self, first_name, last_name, age):
        """initialize new student object

        Args:
            first_name (str): _description_
            last_name (str): _description_
            age (int): _description_
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance

        Args:
            attrs (list, optional):  is a list of strings, only attribute names
                                    contained in this list must be retrieved.
                                    Defaults to None.

        Returns:
            _type_: _description_
        """
        if attrs:
            result = dict()
            for key in attrs:
                result[key] = self.__dict__.get(key)
            return result
        return self.__dict__
