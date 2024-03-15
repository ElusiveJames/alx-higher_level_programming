#!/usr/bin/python3.py
def pow(a, b):
    p = 1
    if b < 0:
        b *= -1
        for i in range(1, b):
            p = a ** (-b)
    else:
        for i in range(1, b+1):
            p = p * a
    return p
