#!/usr/bin/python3
"""
This module defines a Student class that
supports JSON serialization and deserialization.
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

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        using a dictionary.

        This method is used to restore an instance
        from a serialized state (JSON format)
        (e.g., loaded from a file).

        Args:
            json (dict): A dictionary with keys matching attribute names.
        """
        for key, value in json.items():
            setattr(self, key, value)
