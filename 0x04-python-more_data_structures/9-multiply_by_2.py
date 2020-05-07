#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictcopy = a_dictionary.copy()
    for key in dictcopy:
        dictcopy[key] = dictcopy[key] * 2
    return (dictcopy)
