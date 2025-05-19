#!/usr/bin/python3

"""
1-square.py

This module defines a class `Square` that represents a geometric square.

The class includes a private instance attribute `__size`, set through
instantiation but without any type/value validation yet. This is to prepare
for future control over attribute access.
"""


class Square:
    """A class that defines a square with a private size attribute."""
    def __init__(self, size):
        """
        Initializes the square.

        Args:
            size (any): The size of the square (no validation applied).
        """
        self.__size = size
