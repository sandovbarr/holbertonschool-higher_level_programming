#!/usr/bin/python
'''Module 11-student'''


class Student:
    '''init class and return dir'''

    ''' constructor '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    ''' return self dict '''
    def to_json(self):
        return self.__dict__
