#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """Class that define a Sqaure"""

    def __init__(self, size=0):
        """Inintialize a square class

        Args:
            size (int): the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
