#!/usr/bin/python
''' '''


class Student:
    ''' '''

    ''' constructor '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    ''' return self dict '''
    def to_json(self, attrs=None):
        newdict = {}
        if attrs is not None and\
                all(isinstance(el, str) for el in attrs):
            for att in attrs:
                if att in self.__dict__:
                    newdict[att] = self.__dict__[att]
            return newdict
        return self.__dict__
