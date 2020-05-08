#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        key = max(a_dictionary) 
        keyvalue = a_dictionary.get(key)
        return (key, keyvalue)
    else:
        return None
