#!/usr/bin/python3
''' load add and save '''

import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

fname = 'add_item.json'

try:
    content = load_from_json_file(fname) + sys.argv[1:]
except:
    content = sys.argv[1:]
save_to_json_file(content, fname)
