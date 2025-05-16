#!/usr/bin/python3
"""
This module provides a function
that prints a text with 2 new lines
after each of these characters: ., ? and :

"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args: text

    Raise: TypeError if text is not string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    buffer = ""
    for char in text:
        buffer += char
        if char in ".?:":
            print(buffer.strip())
            print()
            buffer = ""
            # make it start fresh for the next line

    # after loop, checking if any part of text ending not ending with .?:
    if buffer.strip():
        print(buffer.strip(), end="")
