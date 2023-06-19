#!/usr/bin/python3
"""
This module contains a class Rectangle
that inherits from BaseGeometry.
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle that inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Instantiation of class.
        width and height must be private. No getter or setter.
        width and height must be positive integers, validated.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
