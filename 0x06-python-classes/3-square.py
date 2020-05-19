#!/usr/bin/python3
"""Square class"""


class Square:
    """Square class with private attribute
    Type of size must be an integer
    otherwise we raise an typeError
    if size is less than 0
    we raise a ValueError for size
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the result of area of a square"""
        return (self.__size * self.__size)
