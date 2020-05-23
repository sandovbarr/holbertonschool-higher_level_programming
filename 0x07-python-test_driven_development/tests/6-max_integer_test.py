#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    class for unnitest
    contains all test for function
    max_integer
    """
    def test_0(self):
        self.assertEqual(max_integer([2, 5, 100]), 100)

    def test_1(self):
        self.assertEqual(max_integer([2, 5, 100, 20, 50]), 100)

    def test_repeated(self):
        self.assertEqual(max_integer([2, 5, 100, 20, 100, 50]), 100)

    def test_negatives(self):
        self.assertEqual(max_integer([-50, -5, -1, -100]), -1)

    def test_floats(self):
        self.assertEqual(max_integer([1.25, 3.45, 7.8, 0.25]), 7.8)

    def test_letters_ascci(self):
        self.assertEqual(max_integer(['a', 'z']), 'z')

    def test_letters_ascci_2(self):
        self.assertEqual(max_integer(['A', 'z']), 'z')

    def test_letters_ascci_3(self):
        self.assertEqual(max_integer(['a', 'Z']), 'a')

    def test_none_case(self):
        self.assertRaises(TypeError, max_integer, [None, None])

    def test_tuples_type(self):
        self.assertEqual(max_integer([(1, 2, 3), (4, 5, 6)]), (4, 5, 6))

    def test_tuples_type_with_string(self):
        self.assertRaises(TypeError, max_integer, ([(1, 2, 3), "holberton"]))

    def test_tuples_type_with_char(self):
        self.assertRaises(TypeError, max_integer, ([(1, 2, 3), 'A']))

    def test_list_tuples_with_letters(self):
        self.assertEqual(max_integer([(1, 2, 3, 'z'), (4, 5, 6)]), (4, 5, 6))
        self.assertEqual(max_integer([(1, 'z'), (6, 'a')]), (6, 'a'))

    def test_bool(self):
        self.assertEqual(max_integer([False, True]), True)
        self.assertEqual(max_integer([False, False]), False)
        self.assertEqual(max_integer([True, False]), True)
        self.assertEqual(max_integer([True, True]), True)
        self.assertEqual(max_integer([1, False]), 1)

    def test_mix_case(self):
        self.assertRaises(TypeError, max_integer, [1, 'str', True])
        self.assertRaises(TypeError, max_integer, [1, [2, 3], True])
        self.assertRaises(TypeError, max_integer, [1, [2, 3], {4, 5}])
        self.assertRaises(TypeError, max_integer, [1, (2, 3), None])

    def test_just_one_number(self):
        self.assertRaises(TypeError, max_integer, 500)
        self.assertRaises(TypeError, max_integer, 5)

if __name__ == "__main__":
    unittest.main()
