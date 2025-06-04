#!/usr/bin/python3
"""
This module defines a function that
returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    This function uses the built-in `json` module to convert a Python object
    into a JSON-formatted string.

    Args:
        my_obj (any): The Python object to convert
        (e.g., dict, list, int, str, etc.)

    Returns:
        str: A JSON-formatted string representing the input object.
    """
    return json.dumps(my_obj)
