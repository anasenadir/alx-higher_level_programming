#!/usr/bin/python3
"""function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str, optional): the filename to be readed. Defaults to "".
    """
    with open(filename, mode="r", encoding="UTF-8") as fd:
        print(fd.read(), end="")
