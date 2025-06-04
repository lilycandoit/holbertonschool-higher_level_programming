#!/usr/bin/python3
"""
The whole purpose — not to convert the
entire object to JSON directly, but to
prepare its attributes in a clean dict form
that JSON can serialize.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of a class instance.

    Args:
        obj: An instance of a class with only serializable attributes.

    Returns:
        dict: Dictionary representation of obj's attributes.
    """
    return obj.__dict__
