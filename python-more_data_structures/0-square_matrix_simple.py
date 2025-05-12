#!/usr/bin/python3

# it works but it is long
# def square_matrix_simple(matrix=[]):
#    new_matrix = []
#     for row in matrix:
#        new_row = list(map(lambda x: x * x, row))
#         new_matrix.append(new_row)
#     return new_matrix

# list comprehension
def square_matrix_simple(matrix=[]):
    return [list(map(lambda x: x * x, row)) for row in matrix]
