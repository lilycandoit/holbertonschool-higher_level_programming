#!/usr/bin/python3
"""This module provides a function to load
an object from a JSON file."""

import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        any: The Python object represented by the JSON content in the file.
    """
    with open(filename, "r") as file:
        return json.load(file)
