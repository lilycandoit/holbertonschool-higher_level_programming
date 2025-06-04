#!/usr/bin/python3
"""
This module defines a function that
writes an Object to a text file in JSON format
"""

import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj (any): The Python object to serialize.
        filename (str): The name of the file to write to.
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
