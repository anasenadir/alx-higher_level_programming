#!/usr/bin/python3
"""Defines a class MagicClass"""
import math


class MagicClass:
    """
    Class that defines properties of MagicClass.

    Attributes:
        radius: radius.
    """
    def __init__(self, radius):
        """Creates new instances of MagicClass.

        Args:
            radius: radius.

        Raises:
            TypeError: radius must be a number .
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Returns area

        Returns: area.
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Returns circumference

        Returns: circumference.
        """
        return 2 * math.pi * self.__radius
