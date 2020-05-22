#!/usr/bin/python3
"""
This module have the function matrix_divided
"""


def matrix_divided(matrix, div):
    """
    Prototype: def matrix_divided(matrix, div):
    matrix must be a list of lists of integers or floats,
    otherwise raise a TypeError exception with the message
    matrix must be a matrix (list of lists)of integers/floats
    Each row of the matrix must be of the same size
    otherwise raise a TypeError exception with the message
    Each row of the matrix must have the same size
    div must be a number (integer or float)
    otherwise raise a TypeError exception with the message
    div must be a number
    div can’t be equal to 0, otherwise raise a ZeroDivisionError
    exception with the message division by zero
    All elements of the matrix should be divided by div
    rounded to 2 decimal places
    Returns a new matrix
    """
    error1 = 'matrix must be a matrix (list of lists) of integers/floats'
    if type(matrix) != list or not matrix or matrix is []:
        raise TypeError(error1)
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    sizeofrow = len(matrix[0])
    for row in matrix:
        if type(row) != list:
            raise TypeError(error1)
        if len(row) != sizeofrow:
            raise TypeError('Each row of the matrix must have the same size')
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(error1)

    newmtx = [[round(elmnt / div, 2) for elmnt in row] for row in matrix]
    return newmtx
