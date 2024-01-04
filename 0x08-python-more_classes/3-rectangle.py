#!/usr/bin/python3
"""
This module containe a class that define a rectangle.
"""


class Rectangle:
    """class Rectangle that defines a rectangle
    """
    def __init__(self, width=0, height=0) -> None:
        """the constractor method of the class

        Args:
            width (int, optional): width of rect. Defaults to 0.
            height (int, optional): heigth of rect. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """return the width value

        Returns:
            int: width value
        """
        return self.__width

    @property
    def height(self):
        """return the height value

        Returns:
            int: height value
        """
        return self.__height

    @width.setter
    def width(self, value):
        """set the value of the width

        Args:
            value (int): the new width value

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.
        """
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")

        if (value < 0):
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """set the value of the height

        Args:
            value (int): the new height value

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.
        """
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")

        if (value < 0):
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Public instance method that returns the rectangle area

        Returns:
            int: return the rect area
        """
        return self.__width * self.height

    def perimeter(self):
        """method that returns the rectangle perimeter
        Perimeter of Rectangle is:

        Returns:
            int: the rectangle perimeter
        """
        if (self.__width == 0 or self.__height == 0):
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """print the rectangle with the character #

        Returns:
            str: rectangle with the character #
        """
        rect = ""
        for _ in range(self.__height):
            rect += "#" * self.width + "\n"

        return rect[:-1]

# if __name__ == "__main__":
#     my_rectangle = Rectangle(2, 4)
#     print("Area: {} - Perimeter: {}
#    ".format(my_rectangle.area(), my_rectangle.perimeter()))

#     print(str(my_rectangle))
#     print(repr(my_rectangle))

#     print("--")

#     my_rectangle.width = 10
#     my_rectangle.height = 3
#     print(my_rectangle)
#     print(repr(my_rectangle))
