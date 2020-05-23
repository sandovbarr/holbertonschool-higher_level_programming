#!/usr/bin/python3
"""
This module have the function add_integer
"""


def add_integer(a, b=98):
    """
    Fuction that returns the add of two integers
    a and b can be integer o floats
    in case of a or b are floats, they must be cast on integers
    Returns an integer: the addition of a and b
    """
    if type(a) != int and type(a) != float:
        raise TypeError('a must be an integer')
    if type(b) != int and type(b) != float:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
