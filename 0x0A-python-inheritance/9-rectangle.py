#!/usr/bin/python3
"""
===================================
module with class Rectangle
===================================
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """BaseGeometry class"""

    def __init__(self, width, height):
        """initialize new Geometry instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """return a hueman readable message"""
        return "[Rectangle {}/{}]".format(self.__width, self.__height)

    def area(self):
        """calculate the area of the reactangle"""
        return self.__width * self.__height
