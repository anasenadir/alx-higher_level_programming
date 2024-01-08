#!/usr/bin/python3
"""class BaseGeometry
"""


class BaseGeometry:
    """BaseGeometry class
    """

    def area(self):
        """instance method that raises an Exception

        Raises:
            Exception: _description_
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value

        Args:
            name (str): _description_
            value (int): _description_
        """
        if (not isinstance(value, int)):
            raise TypeError("{} must be an integer".format(name))

        if (value <= 0):
            raise TypeError("{} must be greater than 0".format(name))
            
