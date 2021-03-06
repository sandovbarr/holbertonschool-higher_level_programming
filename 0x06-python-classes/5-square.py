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

    @property
    def size(self):
        """give us the private attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the private attribute size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints the square based on square"""
        if self.__size == 0:
            print('')
        for n in range(self.__size):
            for m in range(self.__size):
                print('#', end='')
            print('')
