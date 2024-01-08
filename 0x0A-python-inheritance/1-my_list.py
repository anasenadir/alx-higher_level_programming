#!/usr/bin/python3
"""class MyList that inherits from list.
"""


class MyList(list):
    """class that inherits from list

    Args:
        list: the base class
    """
    def print_sorted(self):
        """instance method that prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
