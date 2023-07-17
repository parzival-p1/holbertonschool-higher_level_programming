#!/usr/bin/python3
"""
This module contains a class
with public instance and Raises
exception when required
"""


class BaseGeometry:
    """
    Class Base has 2 public instances methods.
    """
    def area(self):
        """
        Function that raises exception when called.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Function that validates value is an integer.
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
