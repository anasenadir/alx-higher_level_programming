#!/usr/bin/python3
"""Rectangle class Module"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square Class"""
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
