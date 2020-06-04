#!/usr/bin/python3
'''module with append_write'''


def append_write(filename="", text=""):
    '''
        function that appends a string at the end
        of a text file (UTF8) and returns the number
        of characters added:
    '''
    with open(filename, mode="a", encoding='utf-8') as text_file:
        text_file.write(text)
        return (len(text))
