#!/usr/bin/python3
"""
The Square module
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Square class

    Args:
        Rectangle (Class): super class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """the initialize method"""
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """The overloading __str__ method should return:
        [Square](<id>) <x>/<y> - <size> - in our case, width or height
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x,
            self.y, self.width
        )
