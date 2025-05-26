#!/usr/bin/python3

"""
This module defines the `lookup` function.

The `lookup` function returns the list of available attributes
and methods of an object.

This is useful for inspecting objects in Python, similar to
using the built-in `dir()` function.

Functions:
    lookup(obj): Returns the list of available
    attributes and methods of an object.
"""


def lookup(obj):
    """
    Return the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list containing the names of the attributes
        and methods of the object.
    """
    return dir(obj)
