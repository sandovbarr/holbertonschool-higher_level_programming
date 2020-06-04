#!/usr/bin/python3
'''module with read_lines'''


def read_lines(filename="", nb_lines=0):
    '''
        Read_lines put by user
        Read the entire file if nb_lines is lower or equal to 0
        OR greater or equal to the total number of lines of the file
    '''
    cnt_lines = 0
    with open(filename, encoding='utf-8') as text_file:
        if nb_lines <= 0:
            print(text_file.read())
            return
        for line in text_file:
            if cnt_lines < nb_lines:
                print(line.strip())
            cnt_lines += 1
