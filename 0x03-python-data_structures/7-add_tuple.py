#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 1:
        new_a = tuple_a[0]
    else:
        new_a = 0
    if len(tuple_a) >= 2:
        new_b = tuple_a[1]
    else:
        new_b = 0
    if len(tuple_b) >= 1:
        new_a += tuple_b[0]
    if len(tuple_b) >= 2:
        new_b += tuple_b[1]
    result = new_a, new_b
    return result
