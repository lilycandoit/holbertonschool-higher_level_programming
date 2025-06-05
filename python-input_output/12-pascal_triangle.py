#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Build Pascal's triangle iteratively by
    constructing each row based on the previous row.
    """
    if n <= 0:
        return []

    result = []

    for i in range(n):
        # Each row has i+1 elements
        row = [1] * (i + 1)

        # fill in the middle element (if any):
        for j in range(1, i):
            row[j] = result[i-1][j-1] + result[i-1][j]

        result.append(row)
    return result
