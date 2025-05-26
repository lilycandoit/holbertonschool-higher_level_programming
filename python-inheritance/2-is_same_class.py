#!/usr/bin/python3

"""
This module defines the function is_same_class.
"""


def is_same_class(obj, a_class):
    """
    Check if obj is exactly an instance of a_class (not a subclass).

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
