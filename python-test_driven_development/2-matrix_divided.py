#!/usr/bin/python3

"""This module provides a function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """
    All elements of the matrix  divided by div, rounded to 2 decimal places

    Args:
        matrix: A list of lists of integers/floats
        div: A number (int or float) not equal to zero

    Return: a new matrix after division

    Raise:
        TypeError if:
        - matrix is not a list of integers
        - each row not has the same size
        - div is not a number
        ZeroDivisionError if:
        - div is equal to 0
    """

    if not all(isinstance(row, list) for row in matrix):
        TypeError("matrix must be a matrix (list of lists)")
    row_length = len(matrix[0])

    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for e in row:
            if not isinstance(e, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                    )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(e / div, 2) for e in row] for row in matrix]
