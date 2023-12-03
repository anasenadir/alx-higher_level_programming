#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """function that prints a matrix of integers

    You are not allowed to import any module
    You can assume that the list only contains integers
    You are not allowed to cast integers into strings
    You have to use str.format() to print integers
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            s = " " if j != len(matrix) - 1 else ''
            print("{:d}".format(matrix[i][j]), end=s)
            # if j != len(matrix) - 1:
                # print("", end=' ')
        print("")
