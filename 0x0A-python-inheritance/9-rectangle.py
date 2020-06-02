#!/usr/bin/python3
'''
    this module contains
    Rectangle Class
'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    inherits form BaseGeometry
    width and height must be positive integers,
    validated by integer_validator
    '''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        ''' print representation'''
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        return self.__width * self.__height
