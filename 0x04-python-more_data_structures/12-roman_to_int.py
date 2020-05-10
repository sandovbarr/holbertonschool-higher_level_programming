#!/usr/bin/python3
def roman_to_int(roman_string):
    letters = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    value = 0
    for let in range(len(roman_string)):
        if let == len(roman_string) - 1:
                value += letters[roman_string[let]]
        elif letters[roman_string[let]] >= letters[roman_string[let + 1]]:
                value += letters[roman_string[let]]
        else:
                value -= letters[roman_string[let]]
    return value
