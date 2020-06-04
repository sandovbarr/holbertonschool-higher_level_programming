#!/usr/bin/python3
'''module 10-calss_to_json'''


def class_to_json(obj):
    '''Returns dict of instance'''
    return obj.__dict__
