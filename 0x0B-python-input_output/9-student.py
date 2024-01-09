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

    def to_json(self):
        """retrieves a dictionary representation of a Student instance

        Returns:
            dict: dictionary representation
        """
        return self.__dict__
