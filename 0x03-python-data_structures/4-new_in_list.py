#!/bin/usr/python3
def new_in_list(my_list, idx, element):

    new = my_list[:]

    if idx < 0 or idx > len(my_list):
        return (new)
    else:
        new[idx] = element
        return (new)