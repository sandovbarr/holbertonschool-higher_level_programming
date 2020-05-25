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
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    '''str methond'''
    def __str__(self) -> str:
        strto_print = ''
        if self.width == 0 or self.height == 0:
            return strto_print
        for row in range(self.height):
            if row == self.height - 1:
                strto_print += (str(self.print_symbol) * self.width)
            else:
                strto_print += (str(self.print_symbol) * self.width) + '\n'
        return strto_print

    '''repr methond'''
    def __repr__(self) -> str:
        return '{}({}, {})'.format(__class__.__name__, self.width, self.height)

    '''destructor method'''
    def __del__(self):
        print('Bye rectangle...')
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
