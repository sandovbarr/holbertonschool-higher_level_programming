#!/usr/bin/python3
"""
    This module contains
    function print_square
"""


def print_square(size):
    """
    This functions print in stdout
    a square of size received as
    parameter.

    only works with integers > 0
    """
    if type(size) == float and size < 0:
        raise TypeError('size must be an integer')
    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for n in range(size):
        print("#" * size)
