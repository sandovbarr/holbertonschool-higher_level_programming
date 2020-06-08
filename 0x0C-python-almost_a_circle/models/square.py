#!/usr/bin/python3
''' '''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    calls super class constructor
    change his str representation
    '''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return '[Square] ({}) {}/{} - {}'\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    ''' ****** public methods ******'''
    def update(self, *args, **kwargs):
        if len(args) > 0:
            self.id = args[0]
            self.size = args[1] if len(args) == 2 else self.size
            self.x = args[2] if len(args) == 3 else self.x
            self.y = args[3] if len(args) == 4 else self.y
        else:
            self.id = kwargs['id'] if kwargs.get('id') else self.id
            self.size = kwargs['size'] if kwargs.get('size') else self.width
            self.x = kwargs['x'] if kwargs.get('x') else self.x
            self.y = kwargs['y'] if kwargs.get('y') else self.y

    def to_dictionary(self):
        s_rpr = {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
        return (s_rpr)