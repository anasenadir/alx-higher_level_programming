#!/usr/bin/python3

def matrix_divided(matrix, div):
    """All elements of the matrix should be divided by div,
    rounded to 2 decimal places

    Args:
        matrix (list): a list of lists
        div (int/float): an integer or float.
    Return:
        list : return a list of lists.
    >> import doctest
    >> doctest.testfile("tests/2-matrix_divided.txt")
    """
    if (not isinstance(matrix, list)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if (not (isinstance(div, int) or isinstance(div, float))):
        raise TypeError("div must be a number")
    
    if (div == 0):
        raise ZeroDivisionError("division by zero")

    base_list_size = None
    new_matrix = []

    for l_index in range(len(matrix)):
        current_list = matrix[l_index]
        new_matrix.append([])
    
        if (not isinstance(current_list, list)):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        
        for i in range(len(current_list)):
            if (not (isinstance(current_list[i], int) or isinstance(current_list[i], float))):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                
            new_matrix[l_index].append(round(current_list[i] / div, 2))

        if (base_list_size == None):
            base_list_size = len(current_list)
            continue
        
        if (base_list_size != len(current_list)):
            raise TypeError("Each row of the matrix must have the same size")
        
    return new_matrix
