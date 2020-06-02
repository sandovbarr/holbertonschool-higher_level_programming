#!/usr/bin/python3
'''
    this module contains my
    own list class
'''


class MyList(list):
    '''
    Mylist class inherits from
    list. But sorted (ascending sort)
    '''
    def print_sorted(self):
        '''
        just call sorted function to sort
        the list.
        '''
        print(sorted(self))
