#!/usr/bin/python3
for n in range(9):
    for m in range(10):
        if m == n:
            continue
        elif m > n:
            if n == 8 and m == 9:
                print("{}{}".format(n, m))
            else:
                print("{}{}".format(n, m), end=", ")
