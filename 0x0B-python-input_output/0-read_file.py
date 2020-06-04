#!/usr/bin/python3
'''red_file function inside'''


def read_file(filename=""):
    '''
    function that reads a text file
    (UTF8) and prints it to stdout:
    '''
    with open(filename, mode='r', encoding='utf-8') as text_file:
        print(text_file.read(), end='')
