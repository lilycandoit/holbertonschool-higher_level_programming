#!/usr/bin/python3
import json
"""
This module defines a function that
returns the JSON representation of an object (string)
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)

    Args:
        my_obj: the python object
    """
    return json.dumps(my_obj)
