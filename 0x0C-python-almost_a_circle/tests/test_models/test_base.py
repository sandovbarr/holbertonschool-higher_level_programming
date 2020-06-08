#!/usr/bin/python3
""" Base unit testing """
import unittest
import pep8
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseTypos(unittest.TestCase):
    """ Tests base documentation """

    @classmethod
    def setUpClass(cls):
        '''
        is called with the class as the only argument
        and must be decorated as a classmethod():
        '''
        pass

    @classmethod
    def tearDownClass(cls):
        '''
        is called with the class as the only argument
        and must be decorated as a classmethod():
        '''
        pass

    def test_pep8(self):
        """ Test that models/base.py conforms to PEP8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8 Style")

    def test_pep8_base(self):
        """ Test the test file xD """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8 Style")

    def test_docstring(self):
        """test if docstring"""
        self.assertIsNotNone(Base.__doc__)

    def test_docmodule(self):
        """ Tests module """
        self.assertTrue(len(Base.__doc__) >= 1)


class TestBaseFunctions(unittest.TestCase):
    """ Test base class """

    def test_id(self):
        """check id creation"""
        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertIsNotNone(id(b1))

    def test_init(self):
        """check instance"""
        Base._Base__nb_objects = 0
        b2 = Base()
        self.assertIsInstance(b2, Base)

    def test_nb_var(self):
        """check number of objects"""
        Base._Base__nb_objects = 0
        b3 = Base()
        self.assertEqual(b3.id, 1)

    def test_id(self):
        """Checks id´s """
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_json_string(self):
        """ Tests json string function """
        Base._Base__nb_objects = 0
        d1 = {"id": 9, "width": 5, "height": 9, "x": 7, "y": 8}
        d2 = {"id": 10, "width": 3, "height": 15, "x": 4, "y": 0}
        json_string = Base.to_json_string([d1, d2])
        self.assertTrue(type(json_string) is str)
        d = json.loads(json_string)
        self.assertEqual(d, [d1, d2])

    def test_empty_json_string(self):
        """ Send empty string to json function """
        json_string = Base.to_json_string([])
        self.assertTrue(type(json_string) is str)
        self.assertEqual(json_string, "[]")

    def test_None_to_json_String(self):
        """ Send none to json function """
        json_string = Base.to_json_string(None)
        self.assertTrue(type(json_string) is str)
        self.assertEqual(json_string, "[]")

    def test_from_json_string(self):
        """ Regular data to open """
        json_str = '[{"id": 9, "width": 5, "height": 9, "x": 7, "y": 8}, \
                    {"id": 10, "width": 3, "height": 15, "x": 4, "y": 0}]'
        jason_list = Base.from_json_string(json_str)
        self.assertTrue(type(jason_list) is list)
        self.assertEqual(len(jason_list), 2)
        self.assertTrue(type(jason_list[0]) is dict)
        self.assertTrue(type(jason_list[1]) is dict)
        self.assertEqual(jason_list[0],
                         {"id": 9, "width": 5, "height": 9, "x": 7, "y": 8})
        self.assertEqual(jason_list[1],
                         {"id": 10, "width": 3, "height": 15, "x": 4, "y": 0})

    def test_fjs_empty(self):
        """ Send empty string """
        self.assertEqual([], Base.from_json_string(""))

    def test_fjs_None(self):
        """ Send None """
        self.assertEqual([], Base.from_json_string(None))

    def test_saveToFile(self):
        """check save_to_file"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        a_dict = [r1.to_dictionary(), r2.to_dictionary()]  # list dict
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            list_dict = json.loads(file.read())  # list dict
        self.assertTrue(a_dict == list_dict)

    def test_create_fun(self):
        Base._Base__nb_objects = 0
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertTrue(r1 is not r2)
        self.assertTrue(r1 != r2)
