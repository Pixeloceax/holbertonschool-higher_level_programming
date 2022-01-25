#!/usr/bin/python3
""" matrix_divided """


def matrix_divided(matrix, div):
    """
        comment
    """
    size = 0
    if not any(matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if type(i) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for typeN in i:
            if not isinstance(typeN, (int, float)):
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    if matrix[0] is not None:
        size = len(matrix[0])
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if len(i) != size:
        raise TypeError("Each row of the matrix must have the same size")
    return [[round(typeN / div, 2) for typeN in i] for i in matrix]
