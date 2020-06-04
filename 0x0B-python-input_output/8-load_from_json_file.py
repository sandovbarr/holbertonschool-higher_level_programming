#!/usr/bin/python3
'''Contains from_json_string'''

import json


def load_from_json_file(filename):
    '''
    function that creates an Object from a “JSON file”:
    '''
    with open(filename, mode='r', encoding='utf-8') as a_object:
        return json.load(a_object)
