#!/usr/bin/python3
'''
    this module contains
    Rectangle Class
'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    inherits form Rectangle
    size must be private. No getter or setter
    size must be a positive integer, validated by integer_validator

    it will be happens because we now call de init from rectangle
    class, changing the width and height for size and taking
    advantage of their methods like area and __str__

    Now we overwrite the __str__ method to print correctly
    the interpretation for square class
    '''
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
