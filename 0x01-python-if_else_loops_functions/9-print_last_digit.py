#!/usr/bin/ýthon3
def print_last_digit(number):
    if number < 0:
        print(((number * -1) % 10), end="")
        return((number * -1) % 10)
    else:
        print((number % 10), end="")
        return (number % 10)
