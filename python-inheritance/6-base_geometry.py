#!/usr/bin/python3

"""
This module defines an class BaseGeometry with public instance method 'area'
"""


class BaseGeometry:
    """
    Represents a base geometry class.

    Methods:
        area(self):
            Raises an Exception with the message "area() is not implemented".
            This method serves as a placeholder and must
            be implemented by subclasses.
    """
    def area(self):
        """
        Raise an Exception indicating that the area method is not implemented.

        Raises:
            Exception: With the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
