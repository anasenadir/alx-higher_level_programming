#!/usr/bin/python3
"""class MyList that inherits from list.
"""


class MyList(list):
    """class that inherits from list

    Args:
        list: the base class
    """

    def __init__(self, *args):
        super().__init__(*args)

    def print_sorted(self):
        print(sorted(self))
