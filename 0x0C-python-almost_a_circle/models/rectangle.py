#!/usr/bin/python3
"""
The Rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class

    Args:
        Base (Class): super class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """the initialize method

        Args:
            width (int): _description_
            height (int): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (int, optional): _description_. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get the width value
        """
        return self.__width

    @width.setter
    def width(self, width):
        """setter the width

        Args:
            width (int): _description_
        """
        if type(width) != int:
            raise TypeError("width must be an integer.")

        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """get the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """set the height

        Args:
            height (int): _description_
        """
        if type(height) != int:
            raise TypeError("height must be an integer.")

        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """return the get value"""
        return self.__x

    @x.setter
    def x(self, x):
        """set the x

        Args:
            x (int): _description_
        """
        if type(x) != int:
            raise TypeError("x must be an integer.")

        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """return the get value"""
        return self.__y

    @y.setter
    def y(self, y):
        """set the y

        Args:
            y (int): _description_
        """
        if type(y) != int:
            raise TypeError("y must be an integer.")

        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """returns the area value of the Rectangle instance.
        """
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #
        """
        print("\n" * self.__y, end="")
        for _ in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self) -> str:
        """Update the class Rectangle by overriding the __str__ method
        so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x,
            self.__y, self.__width, self.__height
        )
