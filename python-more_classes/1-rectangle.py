#!/usr/bin/python3
"""
Class that defines a rectangle.
"""


class Rectangle:
    """
    This class has two private instance attributes.
    width must be an integer, equal or greater than 0.
    Height must be an integer, equal or greater than 0.
    """

    def __init__(self, width=0, height=0):
        """
        Instantiation with optional width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter: function to retrieve the width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter: validates if value is integer and greater or equal than 0
        Raises:
        TypeError
        ValueError
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter: function to retrieve the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter: validates if value is integer and greater or equal than 0
        Raises:
        TypeError
        ValueError
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
