#!/usr/bin/python3
"""
This module defines a function to appends a string
at the end of a text file (UTF8) and returns
the number of characters added
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file
    and returns the number of characters added.

    Args:
        filename (str): The path to the text file.
        text (str): The string to write into the file.

    Returns:
        int:  the number of characters added.
    """
    with open(filename, "a") as file:
        return file.write(text)
