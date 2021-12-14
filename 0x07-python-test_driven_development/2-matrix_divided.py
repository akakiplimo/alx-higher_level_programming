#!/usr/bin/python3
"""
This module divides all elements of a matrix
It provides one function matrix_divided(matrix, div)
"""
def matrix_divided(matrix, div):
    """Divides all elements of a matrix with div"""
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    size = None
    for l in matrix:
        if type(l) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for i in l:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(j/div, 2) for j in l] for l in matrix]
