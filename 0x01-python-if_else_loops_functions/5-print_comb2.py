#!/usr/bin/python3
for i in range(0, 100):
    if i < 99:
        print(f"{i//10}{i%10}".format(i), end=", ")
    else:
        print(f"{i}".format(i))
