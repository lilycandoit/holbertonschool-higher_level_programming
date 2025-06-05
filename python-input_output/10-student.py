#!/usr/bin/python3
"""
This module defines a class Student with filter that can be serialized to JSON.
"""


class Student:
    """
    Represents a student with first name, last name, and age.

    Public instance attributes:
        - first_name (str)
        - last_name (str)
        - age (int)
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        If `attrs` is a list of strings,
        only return attributes listed in `attrs`.
        Otherwise, return all attributes.

        Args:
            attrs (list or None): List of attribute names to include.

        Returns:
            dict: A dictionary of the selected or all attributes.
        """
        if isinstance(attrs, list):
            # filter the attrbutes belong to the class.
            return {key: self.__dict__[key]
                    for key in attrs if key in self.__dict__}
        return self.__dict__
