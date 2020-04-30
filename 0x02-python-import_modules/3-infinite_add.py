#!/usr/bin/python3

import sys
res = 0

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(0)
    elif len(sys.argv) > 2:
        for i in range(1, len(sys.argv)):
            res += int(sys.argv[i])
        print(res)
