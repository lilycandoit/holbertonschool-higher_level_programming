#!/usr/bin/python3

"""
This module defines an class BaseGeometry with public instance method 'area'
"""


class BaseGeometry:
    """
    Represents a base geometry class with methods for validation.

    Methods:
        area(self):
            Raises an Exception with the message "area() is not implemented".

        integer_validator(self, name, value):
            Validates that 'value' is an integer greater than 0.

            Args:
                name (str): The name of the parameter (for error messages).
                value (int): The value to validate.

            Raises:
                TypeError: If value is not an integer.
                ValueError: If value is <= 0.
    """
    def area(self):
        """
        Raise an Exception indicating that the area method is not implemented.

        Raises:
            Exception: With the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Raise an Exception indicating that the area method is not implemented.

        Raises:
            Exception: With the message "area() is not implemented".
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
