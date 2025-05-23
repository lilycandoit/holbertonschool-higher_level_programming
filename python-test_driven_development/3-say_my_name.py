#!/usr/bin/python3

"""
This module provides a function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    To print a full name

    Args:
        first_name
        last_name

    Raise: TypeError if first_name or last_name is not a string

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if not last_name:
        print("My name is {} ".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))
