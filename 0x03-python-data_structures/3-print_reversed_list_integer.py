#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    function that prints all integers
    of a list, in reverse order.
    -------
    my_list : list
        List of Integers
    """
    if my_list:
        for i in range(len(my_list) - 1, -1, -1):
            print("{:d}".format(my_list[i]))
