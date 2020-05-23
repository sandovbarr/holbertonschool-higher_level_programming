#!/usr/bin/python3
"""
    this module allow us print identation
    using the function text_identation
"""


def text_indentation(text):
    """
    text must be a string, otherwise raise a TypeError
    exception with the message text must be a string
    There should be no space at the beginning
    or at the end of each printed line
    """

    auxstr = ""
    if type(text) != str:
        raise TypeError('text must be a string')
    for letter in range(len(text)):
        if text[letter] not in ['.', '?', ':']:
            auxstr += text[letter]
        else:
            auxstr += text[letter]
            print("{}".format(auxstr.strip()))
            print()
            auxstr = ""
    print("{}".format(auxstr.strip()), end="")
