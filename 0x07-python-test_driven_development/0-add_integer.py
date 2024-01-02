#!/usr/bin/python3

def add_integer(a, b=98):
    """function return the sum of two integers

    Args:
        a (int): the first number.
        b (int, optional): the second number. Defaults to 98.

    Raises:
        TypeError: if a or b is not integers.

    Returns:
        int : the sum of the two numbers.
    
    >> import doctest
    >> doctest.testfile("tests/0-add_integer.txt")
    """
    if (isinstance(a, float)):
        a = int(a)
    if (isinstance(b, float)):
        b = int(b)
    
    if (not isinstance(a, int)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int)):
        raise TypeError("b must be an integer")

    return a + b
