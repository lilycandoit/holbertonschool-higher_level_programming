#!/usr/bin/python3
"""
This module defines a class Student that can be serialized to JSON.
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

    def to_json(self):
        """
        Retrieves a dictionary representation of the Student instance.

        Returns:
            dict: A dictionary containing all serializable attributes.
        """
        return self.__dict__
