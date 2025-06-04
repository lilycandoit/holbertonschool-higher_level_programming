#!/usr/bin/python3
"""
This module defines a function to read
and print the content of a text file (UTF-8).

It demonstrates basic file input/output
in Python using the `with` statement.

The function does not handle exceptions
and assumes the file exists and is readable.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its content to stdout.

    Args:
        filename (str): The path to the text file to be read.

    Returns:
        None
    """
    with open(filename, "r") as file:
        content = file.read()
        print(content)
