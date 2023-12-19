#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """Class that define a Sqaure"""

    def __init__(self, size=0, position=(0, 0)):
        """Inintialize a square class

        Args:
            size (int): the size of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the position of the sequare"""
        return self.__position

    @position.setter
    def position(self, position):
        """Set the position of the square

        Args:
            position (tuple): must be a tuple of 2 positive integers
        """
        if (not isinstance(position, tuple) or len(position) != 2 or
                not all(isinstance(item, int) for item in position) or
                not all(item >= 0 for item in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """returns the current square area"""
        return self.size ** 2

    def my_print(self):
        """ prints in stdout the square with the character #"""
        if self.size == 0:
            print()
            return

        [print("") for _ in range(self.position[1])]
        for row in range(self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size)
