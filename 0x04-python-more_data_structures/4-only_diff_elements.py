#!/usr/bin/python3
def common_elements(set_1, set_2):
    uniquements = (set_1 | set_2)  - (set_1 & set_2)
    return uniquements
