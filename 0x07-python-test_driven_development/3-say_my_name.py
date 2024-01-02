#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """_summary_

    Args:
        first_name (str): first name
        last_name (str, optional): last name. Defaults to "".

    Raises:
        TypeError: if first_name or last_name are not strings

    >> import(doctest) 
    >> doctest.testfile("tests/3-say_my_name.txt")
    """
    if (not isinstance(first_name, str) or first_name == None):
        raise TypeError("first_name must be a string")    

    if (not isinstance(last_name, str)):
        raise TypeError("last_name must be a string")    

    print("My name is {} {}".format(first_name, last_name))
