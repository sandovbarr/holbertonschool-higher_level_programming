#!/usr/bin/python3

import sys

word = "argument"
word2 = ":"

if len(sys.argv) < 2:
   print("0 arguments.")
if len(sys.argv) == 2:
    print("{:d} {:s}{:s}".format(len(sys.argv) - 1, word, word2))
    print("{:d}: {:s}".format(len(sys.argv) - 1, sys.argv[1]))
elif len(sys.argv) > 2:
    word = "arguments"
    word2 = ":"
    print("{} {}{}".format(len(sys.argv) - 1, word, word2))
    for i in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(i, sys.argv[i]))
