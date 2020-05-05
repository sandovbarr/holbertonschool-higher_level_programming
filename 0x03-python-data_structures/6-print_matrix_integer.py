#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        it = 0
        for j in i:
            if it == len(i) - 1:
                print("{:d}".format(j), end="")
            else:
                print("{:d}".format(j), end=" ")
            it += 1
        print('')
