#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortdict = sorted(a_dictionary.items())
    newdict = dict(sortdict)
    for key in newdict:
        print (key, ":", newdict[key])
