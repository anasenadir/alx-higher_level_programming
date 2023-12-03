#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    function that replaces an element of a list at a
    specific position (like in C).
    ---------
    my_list : list
        List of integers
    idx : int
        The index of item to be changed
    element : int
        The new Value
    """
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    my_list[idx] = element
    return (my_list)
