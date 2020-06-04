#!/usr/bin/python3
'''Contains from_json_string'''
import json


def save_to_json_file(my_obj, filename):
    '''
    function that writes an Object to a text file,
    using a JSON representation:
    '''
    with open(filename, mode="w", encoding='utf-8') as json_file:
        json_file.write(json.dumps(my_obj))
