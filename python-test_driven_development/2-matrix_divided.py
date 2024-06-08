#!/usr/bin/python3

"""
    matrix_divided - containing module
"""


def matrix_divided(matrix: list, div: int):
    """
        divides all elements of matrix
    """
    listError = 'matrix must be a matrix (list of lists) of integers/floats'
    sizeError = 'Each row of the matrix must have the same size'
    if not isinstance(matrix, (list)):
        raise TypeError(listError)
    if div == 0.0 or div == 0:
        raise ZeroDivisionError('division by zero')
    for row in matrix:
        if not all(isinstance(i, (int, float)) for i in row):
            raise TypeError(listError)
        if len(row) != len(matrix[0]):
            raise TypeError(sizeError)
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    return [[round(i / div, 2) for i in row] for row in matrix]
