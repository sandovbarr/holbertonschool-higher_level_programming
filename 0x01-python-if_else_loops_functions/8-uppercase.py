#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        ascichar = ord(str[i])
        if ((ascichar >= 65 and ascichar <= 90) or
           (ascichar >= 48 and ascichar <= 57) or ascichar == 32):
            c = str[i]
        else:
            c = chr(ord(str[i]) - 32)
        print("{}".format(c), end="")
    print("")
