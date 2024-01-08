#!/usr/bin/python3
"""function that returns True if the object is an instance
of, or if the object is an instance of a
class that inherited from, the specified class ;
otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """function that returns True if the object is an instance
    of, or if the object is an instance of a
    class that inherited from, the specified class ;
    otherwise False.

    Args:
        obj (obj): _description_
        a_class (class): _description_
    """
    return isinstance(obj, a_class)
