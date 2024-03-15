#!/usr/bin/python3
def uppercase(str):
    str_2 = ''
    for i in str:
        if ord(i) >= 97 and ord(i) < 123:
            str_2 += chr(ord(i) - 32)
        else:
            str_2 += i
    print(f"{str_2}". format())
