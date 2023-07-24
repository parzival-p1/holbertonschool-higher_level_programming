#!/usr/bin/python3
"""
This module contains the class Square that inherits from Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class contains instantiation of the class Square
    that inherits from Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Call the super class with id, x, y, width and height.
        The width and height must be assigned to the value of size.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Overloading __str__ method should return [Square]
        (<id>) <x>/<y> - <size>
        """
        return ("[Square] ({}) {:d}/{:d} - {:d}".format
                (self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """
        This function returns the size (Getter).
        You can return either width or height since they are the same.
        """
        return (self.width)

    @size.setter
    def size(self, value):
        """
        The setter should assign (in this order) the width and the
        height - with the same value.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update 2 the class Square by adding the public method update
        that assigns an argument to each attribute.
        Using *args or **kwargs.
        """
        if len(args):
            for i, _arg in enumerate(args):
                if i == 0:
                    self.id = _arg
                if i == 1:
                    self.size = _arg
                if i == 2:
                    self.x = _arg
                if i == 3:
                    self.y = _arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        Public method that returns the dictionary  of a Square.
        This dictionary must contain: id, size, x and y.
        """
        d = {}
        d["id"] = self.id
        d["size"] = self.size
        d["x"] = self.x
        d["y"] = self.y
        return d
