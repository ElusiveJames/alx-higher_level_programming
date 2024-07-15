#!/usr/bin/python3
output = ""
for i in range(122, 97, -2):

    output += "{:c}{:c}".format(i, i-33)
print(output, end="")
