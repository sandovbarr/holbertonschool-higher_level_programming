#!/usr/bin/python3
'''
    module with number_of_lines
'''


def number_of_lines(filename=""):
    '''
    Number of lines
    '''
    cnt_lines = 0
    with open(filename, mode='r', encoding='utf-8') as text_file:
        for lines in text_file:
            cnt_lines += 1
    return (cnt_lines)
