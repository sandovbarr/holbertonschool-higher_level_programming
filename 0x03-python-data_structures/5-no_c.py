#!/usr/bin/python3
def no_c(my_string):
    # we define letters that can't be included
    letters = "Cc"
    # this is the new string
    not_c = ""
    for letterofstr in my_string:
        if letterofstr not in letters:
            not_c += letterofstr
    return not_c
