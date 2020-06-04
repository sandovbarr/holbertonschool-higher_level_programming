#!/usr/bin/python3
'''module with write_file'''


def write_file(filename="", text=""):
    '''
        function that write a string to a text file
        (UTF8) and returns the number of characters written:
    '''
    with open(filename, mode="w", encoding='utf-8') as text_file:
        text_file.write(text)
        return (len(text))
