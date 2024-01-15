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
        """square update method"""
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """return the dictionary represintation of the react object"""
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
