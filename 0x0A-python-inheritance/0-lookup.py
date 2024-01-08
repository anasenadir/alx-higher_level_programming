#!/usr/bin/python3
"""function that returns the list of available attributes
"""


def lookup(obj):
    """function that returns the list of available attributes

    Args:
        obj (obj): the object var
    """
    return dir(obj)
