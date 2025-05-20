#!/usr/bin/python3
"""
4-square.py

This module defines a class Square with:
- Private size attribute
- Property getter and setter with validation
- Area calculation method
- Prints in stdout the square with the character #
"""


class Square:
    """A class that defines a square by its size and can compute area."""
    __size = 0

    def __init__(self, size = 0, position = (0, 0)):
        """
        Initialize the square.

        Args:
            size (int): Size of the square, must be >= 0
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Property getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Property setter for size with validation.

        Args:
            value (int): The new size to set

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """ getter to read position """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter for position validation and to update position
        """
        if (
            not isinstance(value, tuple)
            or not all(isinstance(n, int) for n in value)
            or not all(n >= 0 for n in value)
            or len(value) != 2
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the current square area.

        Returns:
            int: The area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        To print the area with character # and respecting position
        """

        if self.__size == 0:
            print()

        # print vertical positions (blank lines)
        for _ in range (self.__position[1]):
            print()

        # print each row
        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            for _ in range(self.__size):
                print("#", end="")
            print()

        # other shorter way but more abstract
        # for _ in range(self.__size):
        #    print(" " * self.__position[0] + "#" * self.__size)
