#!/usr/bin/python3
"""function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)
    and returns the number of characters written

    Args:
        filename (str, optional): the name of the file. Defaults to "".
        text (str, optional): text to be written. Defaults to "".
    """
    with open(filename, mode="w", encoding="UTF-8") as fd:
        return fd.write(text)
