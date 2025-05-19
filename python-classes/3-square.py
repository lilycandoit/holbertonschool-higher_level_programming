#!/usr/bin/python3

"""
3-square.py

This module defines a class `Square` with:
- a private attribute `__size`
- validation for type and value
- a public method `area()` to return the square's area
"""


class Square:
    """A class that defines a square by its size and can compute area."""
    def __init__(self, size=0):
        """
        Initialize the square.

        Args:
            size (int): Size of the square, must be >= 0

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the current square area.

        Returns:
            int: The area of the square
        """
        return self.__size * self.__size
