#!/usr/bin/ýthon3
def print_last_digit(number):
    if number < 0:
        last = (number * -1) % 10
        print(last, end="")
        return(last)
    else:
        last = number % 10
        print(last, end="")
        return (last)
