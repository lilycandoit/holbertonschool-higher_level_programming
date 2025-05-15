#!/usr/bin/python3
"""
    This module provides a function that prints a square with the character #.
"""


def print_square(size):
    """
    A function that prints a square with the character #.

    Raise: TypeError
        - size must be an integer
        - size must be >= 0
        - size must be an integer

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for row in range(size):
        for e in range(size):
            print("#", end="")
        print()
