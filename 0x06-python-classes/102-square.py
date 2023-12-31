#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """Class that define a Sqaure"""

    def __init__(self, size=0):
        """Inintialize a square class

        Args:
            size (int): the size of the square
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the squrae"""
        return self.__size

    @size.setter
    def size(self, size):
        """sets the size of the sequare

        Args:
            size (int): the size of the sequare
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current square area"""
        return self.size ** 2

    def __eq__(self, _sequare):
        return self.size == _sequare.size

    def __le__(self, _sequare):
        return self.size <= _sequare.size

    def __ge__(self, _sequare):
        return self.size >= _sequare.size

    def __lt__(self, _sequare):
        return self.size < _sequare.size

    def __gt__(self, _sequare):
        return self.size > _sequare.size

    def __ne__(self, _sequare):
        return self.size != _sequare.size
