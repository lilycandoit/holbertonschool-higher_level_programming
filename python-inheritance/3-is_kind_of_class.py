#!/usr/bin/python3

"""
This module defines the function is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if obj is an instance of a_class or a subclass of a_class.

    This function returns True if the object is an instance
    of the specified class
    or if it is an instance of a class that inherited from the specified class.
    Otherwise, it returns False.

    Args:
        obj: The object to check.
        a_class: The class or superclass to compare against.

    Returns:
        True if obj is an instance of a_class or
        a subclass of a_class, False otherwise.
    """
    return isinstance(obj, a_class)
