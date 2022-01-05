#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    list1 = []
    for x in matrix:
        list1.append(list(map(lambda x: x**2, x)))
    return (list1)
