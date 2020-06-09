#!/usr/bin/python3
'''
    Square class
    import from rectangle
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    calls super class constructor
    change his str representation
    '''

    def __init__(self, size, x=0, y=0, id=None):
        ''' constructor '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        ''' str representation '''
        return '[Square] ({}) {}/{} - {}'\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        ''' geter '''
        return self.width

    @size.setter
    def size(self, value):
        ''' seter '''
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    ''' ****** public methods ******'''
    def update(self, *args, **kwargs):
        ''' update by args o kwargs '''
        if len(args):
            counter = 0
            keys = ['id', 'size', 'x', 'y']
            for value in args:
                if counter < 4:
                    setattr(self, keys[counter], value)
                    counter += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        ''' return a dict representation '''
        s_rpr = {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
        return (s_rpr)
