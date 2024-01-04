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

    def area(self):
        """Public instance method that returns the rectangle area"""
        return self.__width * self.height

    def perimeter(self):
        """method that returns the rectangle perimeter
        Perimeter of Rectangle is:
            -> 2 (width + height)
        """
        if (self.__width == 0 and self.__height == 0):
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """print the rectangle with the character #"""
        rect = ""
        for _ in range(self.__height):
            rect += "#" * self.width + "\n"

        return rect[:-1]

    def __repr__(self) -> str:
        """return a string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """
        return "{}({}, {})".format(__class__.__name__,
                                   self.__width, self.__height)


# if __name__ == "__main__":
#     my_rectangle = Rectangle(2, 4)
#     print(str(my_rectangle))
#     print("--")
#     print(my_rectangle)
#     print("--")
#     print(repr(my_rectangle))
#     print("--")
#     print(hex(id(my_rectangle)))
#     print("--")

    # create new instance based on representation
    # new_rectangle = eval(repr(my_rectangle))
    # print(str(new_rectangle))
    # print("--")
    # print(new_rectangle)
    # print("--")
    # print(repr(new_rectangle))
    # print("--")
    # print(hex(id(new_rectangle)))
    # print("--")

    # print(new_rectangle is my_rectangle)
    # print(type(new_rectangle) is type(my_rectangle))
