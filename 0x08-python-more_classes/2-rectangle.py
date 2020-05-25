#!/usr/bin/python3
'''
    this module contains the class:
    Rectangle
'''


class Rectangle:
    '''
    class to take
    an width and height
    to define a rectangle
    '''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    '''getter for width'''
    @property
    def width(self):
        return self.__width

    '''setter for width'''
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    '''getter for height'''
    @property
    def height(self):
        return self.__height

    '''setter for height'''
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    '''public instante method'''
    def area(self):
        return (self.__width * self.__height)

    '''public instante method'''
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return (0)
        return (2 * (self.__width + self.__height))
