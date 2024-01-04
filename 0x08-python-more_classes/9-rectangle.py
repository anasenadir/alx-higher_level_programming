#!/usr/bin/python3
"""
This module containe a class that define a rectangle.
"""


class Rectangle:
    """class Rectangle that defines a rectangle

    Attributes:
        number_of_instances (int): number of instaices
        print_symbol (any): Used as symbol for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0) -> None:
        __class__.number_of_instances += 1
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
        # print(__class__.print_symbol)
        # return rect
        for _ in range(self.__height):
            rect += str(self.print_symbol) * self.width + "\n"

        return rect[:-1]

    def __repr__(self) -> str:
        """return a string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """
        return "{}({}, {})".format(__class__.__name__,
                                   self.__width, self.__height)

    def __del__(self):
        """function that the message "Bye rectangle..." when an
        instance of Rectangle is deleted
        """
        __class__.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method that returns
        the biggest rectangle based on the area"""
        if (not isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if (not isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if (rect_1.area() >= rect_2.area()):
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Class method that returns a new
        Rectangle instance with width == height == size"""
        return cls(size, size)

# if __name__ == "__main__":
#     my_square = Rectangle.square(5)
#     print("Area: {} - Perimeter: {}"
#    .format(my_square.area(), my_square.perimeter()))
#     print(my_square)
