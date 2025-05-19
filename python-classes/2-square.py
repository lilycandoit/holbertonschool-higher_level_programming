#!/usr/bin/python3
"""
2-square.py

This module defines a class `Square` that validates size during instantiation.

Raises:
    TypeError: If `size` is not an integer
    ValueError: If `size` is less than 0
"""


class Square:
    """A class that defines a square with size validation."""
    def __init__(self, size=0):
        """
        Initializes the square with optional size (default is 0).

        Args:
            size (int): Size of the square (must be >= 0)

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
