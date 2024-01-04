#!/usr/bin/python3
"""
This module containe a class that define a rectangle.
"""


class Rectangle:
    """class Rectangle that defines a rectangle"""
    def __init__(self, width=0, height=0) -> None:
        self.width = width
        self.height = height

    @property
    def width(self):
        """return the width value"""
        return self.__width

    @property
    def height(self):
        """return the height value"""
        return self.__height

    @width.setter
    def width(self, value):
        """set the width of the rectangle
        (Args):
            value (int): the new width value
        """

        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")

        if (value < 0):
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """set the value of the height

        (Args):
            value (int): the new height value
        """
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")

        if (value < 0):
            raise ValueError("height must be >= 0")

        self.__height = value

# if __name__ == "__main__":
#     my_rectangle = Rectangle(2, 4)
#     print(my_rectangle.__dict__)

#     my_rectangle.width = 10
#     my_rectangle.height = 3
#     print(my_rectangle.__dict__)
