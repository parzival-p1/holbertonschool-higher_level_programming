#!/usr/bin/python3
"""
This module contains a class Rectangle that inherits from Base.
"""
from models.base import Base


class Rectangle(Base):
    """
    This is the class Rectangle containing Private instance attributes,
    each with its own public getter and setter:
    Attributes __width,  __height, __x and __y and a class constructor.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor. Call the super class with id then Assign each
        argument width, height, x and y to the right attribute.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Returns the width.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Setter receives and validates value as param.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Return the height.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Setter receives and validates value as param.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Returns the x.
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        Setter receives and validates value as param.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Returns the y.
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        Setter receives and validates value as param.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Public method that returns the area value of the instance.
        """
        return (self.__width * self.__height)

    def display(self):
        """
        Public method that prints in stdout the Rectangle instance with
        the character #.
        """
        print(("\n" * self.__y) + "\n".join(((" " * self.__x) +
                                             ("#" * self.__width))
                                            for a in range(self.__height)))

    def __str__(self):
        """
        This function overrides the __str__ method so that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".
                format(self.id, self.__x, self.__y, self.__width,
                       self.__height))

    def update(self, *args, **kwargs):
        """
        Update 2 the class Rectangle by adding the public method update
        that assigns an argument to each attribute.
        Using *args or **kwargs.
        """
        if len(args):
            for i, _arg in enumerate(args):
                if i == 0:
                    self.id = _arg
                elif i == 1:
                    self.width = _arg
                elif i == 2:
                    self.height = _arg
                elif i == 3:
                    self.x = _arg
                elif i == 4:
                    self.y = _arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        Public method that returns the dictionary  of a Rectangle.
        This dictionary must contain: id, width, height, x and y.
        """
        d = {}
        d["id"] = self.id
        d["width"] = self.width
        d["height"] = self.height
        d["x"] = self.x
        d["y"] = self.y
        return d
