#!/usr/bin/python3
"""
This module contains a class
with public instance and Raises
exception when required
"""


class BaseGeometry:
    """
    A class Base has public instance method.
    """
    def area(self):
        """
        Function that raises exception when called.
        """
        raise Exception("area() is not implemented")
