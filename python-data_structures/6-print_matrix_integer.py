#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in range(len(row)):
            end_char = ' ' if num < len(row) - 1 else ''
            print("{:d}".format(num), end=end_char)
        print()
