#!/usr/bin/python3
"""
this module contains the funcion that validates
name and last name, both must be strings
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name function
    first validate that first_name is an string
    otherwise raise a TypeError request data type
    then last_name is also validated to verify the same
    otherwise will raise same TypeError

    The function don't have return, just print with format
    the complete name.

    if an argument pass like a string for instance '1425'
    it will be allowed to be printed
    """
    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    if type(last_name) != str:
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))
