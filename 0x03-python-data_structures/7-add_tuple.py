#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1 and len(tuple_b) == 2:
        int1 = tuple_a[0] + tuple_b[0]
        int2 = tuple_b[1]
    elif len(tuple_b) == 1 and len(tuple_a) == 2:
        int1 = tuple_a[0] + tuple_b[0]
        int2 = tuple_a[1]
    elif len(tuple_a) == 0 and len(tuple_b) == 2:
        return tuple_b
    elif len(tuple_a) == 2 and len(tuple_b) == 0:
        return tuple_a
    else:
        int1 = tuple_a[0] + tuple_b[0]
        int2 = tuple_a[1] + tuple_b[1]
    tuple_c = (int1, int2)
    return tuple_c
