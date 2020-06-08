#!/usr/bin/python3
''' Module with base class '''


import json


class Base:
    '''
    private class attribute __nb_objects = 0
    class constructor: def __init__(self, id=None)::
    '''

    __nb_objects = 0

    ''' constructor '''
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is not None or []:
            return json.dumps(list_dictionaries)
        else:
            return ([])

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        filename, contains class name + .json extension
        create a empty list
        iterate trought list_objects
        append the element converted to diciontary repres

        open the file as f
        create a variable jsonstrings that contains the list
        of elements and convert it to a json string usign this method
        finally write into file f this content.
        '''
        filename = cls.__name__ + ".json"
        elements = []
        for el in list_objs:
            elements.append(el.to_dictionary())

        with open(filename, 'w') as f:
            jsonstrings = cls.to_json_string(elements)
            f.write(jsonstrings)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or "":
            return ([])
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            dummyinst = cls(1,1)
        if cls.__name__ == 'Square':
            dummyinst = cls(1,1)
        dummyinst.update(**dictionary)
        return dummyinst

    @classmethod
    def load_from_file(cls):
        try:
            with open(cls.__name__ + '.json', 'r') as f:
                '''retornar la lista de instancias'''
                fileopen = f.open()
                
        except:
            return ([])



