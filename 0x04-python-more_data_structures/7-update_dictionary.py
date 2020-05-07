#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    dictaux = {key : value}
    a_dictionary.update(dictaux)
    return (a_dictionary)
