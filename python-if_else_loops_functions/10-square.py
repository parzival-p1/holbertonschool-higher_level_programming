#!/usr/bin/python3
"""
This module contains a class Square that
inherits from Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from rectangle.
    """
    def __init__(self, size):
        """
        Class instantiation.
        size must be private. No getter or setter.
        size must be a positive integer, validated.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"Returns the area of the square"""
        return self.__size ** 2
