#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        for value in item:
            print("{:d}".format(value), end='')
            if (value is not item[len(item) - 1]):
                print(" ", end="")
        print()
