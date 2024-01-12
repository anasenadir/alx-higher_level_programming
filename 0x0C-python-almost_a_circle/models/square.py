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

    @property
    def size(self):
        """return the size value"""
        return self.width

    @size.setter
    def size(self, value):
        """update the value of the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        params = ["id", "size", "x", "y"]

        for index, value in enumerate(args):
            if index >= len(params):
                break
            if params[index] not in kwargs:
                setattr(self, params[index], value)

        for key, value in kwargs.items():
            if key in params:
                setattr(self, key, value)
