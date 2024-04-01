#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_2 = []
    for elements in matrix:
        matrix_2.append(list(map(lambda x: x**2, elements)))
    return matrix_2
