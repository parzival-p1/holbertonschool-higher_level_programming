#!/usr/bin/python3
"""
Class that defines a rectangle.
"""


class Rectangle:
    """
    This class has two private instance attributes.
    width must be an integer, equal or greater than 0.
    Height must be an integer, equal or greater than 0.
    This class has two Public class attribute.
    number_of_instances, that stores the number of instances done.
    print_symbol, symbol used for string representation.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Instantiation with optional width and height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        Returns area of a rectangle using given width and height
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Returns perimeter of a rectangle using given width and height
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """
        Returns string of Rectangle using #
        if 0 returns empty string
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        width = ("{}".format(self.print_symbol)) * self.__width
        rectangle = width
        for x in range(self.__height - 1):
            rectangle += "\n" + width
        return (rectangle)

    def __repr__(self):
        """
        Returns a string representation
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """
        Prints when deleting an instance
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the bigger rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() < rect_2.area():
            return (rect_2)
        return (rect_1)

    @classmethod
    def square(cls, size=0):
        """
        returns new rect where width == height == size
        """
        return (cls(size, size))
