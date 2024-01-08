#!/usr/bin/python3
"""function that returns True if the
object is exactly an instance of the specified class ;
otherwise False.
"""


def is_same_class(obj, a_class):
    """function that returns True if the
    object is exactly an instance of the specified class ;
    otherwise False.

    Args:
        obj (obj): _description_
        a_class (class): _description_
    """
    if (type(obj) == a_class):
        return True
    return False
