#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        ascichar = ord(str[i])
        if ascichar >= 97 and ascichar <= 122:
            c = chr(ascichar - 32)
        else:
            c = chr(ascichar)
        print("{}".format(c), end="")
    print("")
