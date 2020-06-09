#!/usr/bin/python3
'''
    Rectangle class module
    import form base module
'''

from models.base import Base


class Rectangle(Base):
    '''
    Rectangle Class
    __
    Private instance attributes, each with its own public getter and setter:
    __width -> width
    __height -> height
    __x -> x
    __y -> y
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' constructor '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        ''' getter '''
        return self.__width

    @property
    def height(self):
        ''' getter '''
        return self.__height

    @property
    def x(self):
        ''' getter '''
        return self.__x

    @property
    def y(self):
        ''' getter '''
        return self.__y

    @width.setter
    def width(self, value):
        ''' seter '''
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        ''' seter '''
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        ''' seter '''
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        ''' seter '''
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        ''' computes rectangle area '''
        return self.__width * self.__height

    def display(self):
        ''' prints in stdout the Rectangle instance with the character #'''
        for times in range(self.__y):
            print()
        for rows in range(self.__height):
            print(" " * self.__x, end="")
            print('#' * self.__width)

    def __str__(self):
        ''' returns str representation '''
        return '[Rectangle] ({}) {}/{} - {}/{}'\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        ''' update by args or kwargs '''
        if len(args) > 0:
            super().__init__(args[0])
            self.width = args[1] if len(args) == 2 else self.__width
            self.height = args[2] if len(args) == 3 else self.__height
            self.x = args[3] if len(args) == 4 else self.__x
            self.y = args[4] if len(args) == 5 else self.__y
            return
        else:
            super().__init__(kwargs['id'])\
                if kwargs.get('id') else self.id
            self.width = kwargs['width']\
                if kwargs.get('width') else self.__width
            self.height = kwargs['height']\
                if kwargs.get('height') else self.__height
            self.x = kwargs['x'] if kwargs.get('x') else self.__x
            self.y = kwargs['y'] if kwargs.get('y') else self.__y

    def to_dictionary(self):
        ''' create a representation '''
        r_rpr = {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.__height,
            'width': self.__width
            }
        return (r_rpr)
