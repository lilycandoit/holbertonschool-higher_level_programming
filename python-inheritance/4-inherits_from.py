#!/usr/bin/python3
"""
This module defines the function inherits_from.
"""


def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a class that inherited
    (directly or indirectly) from a_class.

    The object must not be an exact instance of a_class.
    It must be a subclass or child class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj's class is a subclass of a_class
        (not the same), False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
