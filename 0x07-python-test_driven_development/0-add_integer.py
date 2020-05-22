#!/usr/bin/python3
"""This module have the function add_integer """


def add_integer(a, b=98):
    """ 
    Fuction that returns the add of two integers
    a and b can be integert o floats
    in case of a or b are floats, they must be cast on integers
    Returns an integer: the addition of a and b
    """
    try:
        int(a)
    except (ValueError, TypeError):
        raise TypeError ('a must be an integer')
    try:
        int(b)
    except (ValueError, TypeError):
        raise TypeError ('b must be an integer')
    return int(a) + int(b)
