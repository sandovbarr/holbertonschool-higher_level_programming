#!/usr/bin/python3
''' Module with base class '''


import json


class Base:
    '''
    private class attribute __nb_objects = 0
    class constructor: def __init__(self, id=None)::
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        ''' constructor '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' Returns a json string '''
        if list_dictionaries is not None or []:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

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
        elements = []
        if list_objs is not none:
            for el in list_objs:
                elements.append(el.to_dictionary())
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            jsonstrings = cls.to_json_string(elements)
            f.write(jsonstrings)

    @staticmethod
    def from_json_string(json_string):
        """returns the dictionary representation of a Square"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        ''' creates a list of dicts '''
        if cls.__name__ == 'Rectangle':
            dummyinst = cls(1, 1)
        if cls.__name__ == 'Square':
            dummyinst = cls(1)
        dummyinst.update(**dictionary)
        return dummyinst

    @classmethod
    def load_from_file(cls):
        ''' loads from file and creates the list '''
        try:
            with open(cls.__name__ + '.json', 'r', encoding='utf-8') as file:
                '''retornar la lista de instancias'''
                listofinstances = []
                data = cls.from_json_string(file.read())
                for element in data:
                    listofinstances.append(cls.create(**element))
                return(listofinstances)
        except:
            return ([])
