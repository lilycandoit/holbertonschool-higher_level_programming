#!/usr/bin/python3
"""
This module defines a function to write string
into a text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8)
    and returns the number of characters written.

    Args:
        filename (str): The path to the text file.
        text (str): The string to write into the file.

    Returns:
        int: Number of characters written to the file.
    """
    with open(filename, "w") as file:
        return file.write(text)
