#!/usr/bin/python3

"""This module provides a function to add two integers."""


def add_integer(a, b=98):

    """
    Adds two integers or floats (casted to int).

    Args:
        a: First number
        b: Second number (default is 98)

    Returns:
        The integer sum of a and b

    Raises:
        TypeError: If a or b is not an int or float
    """

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    elif not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
