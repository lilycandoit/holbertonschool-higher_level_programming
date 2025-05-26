#!/usr/bin/python3

"""
This module defines a class Square that inherited from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square shape, inherits from Rectangle.
    """
    def __init__(self, size):
        """
        Initialize a square with size.

        size must be a positive integer, validated by integer_validator

        Args:
            size (int)
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculate and return the area of the square
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Return a string representation of the Square object.

        Format:
            [Rectangle] <size>/<size>

        Returns:
            str: Formatted string describing the square's dimensions.
        """
        return ("[{}] {}/{}".format(type(self).__name__, self.__size, self.__size))
