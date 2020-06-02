#!/usr/bin/python3
'''
    this module contains:
    is_same_calss
'''


def is_same_class(obj, a_class):
    '''
    is_sae_class - function that
    returns True if the object is exactly an instance
    of the specified class ; otherwise False.
    '''
    return(type(obj) == a_class)
