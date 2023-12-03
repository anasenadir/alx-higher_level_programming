#!/usr/bin/python3
def element_at(my_list, idx):
    """
    function that retrieves an
    element from a list like in C.
    -----------
    my_list : list
        A list of integers
    idx : int
        Index of an item
    """
    if idx < 0 or idx >= len(my_list):
        return (None)
    return my_list[idx]
