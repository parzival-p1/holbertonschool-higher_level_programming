#!/usr/bin/python3
"""
This modules contains a class
that inherits from int
"""


class MyInt(int):
    """
    MyInt is a rebel. MyInt has == and != operators inverted.
    """
    def __eq__(self, other):
        """
        Returns the opposite for the == operator.
        """
        return (not super().__eq__(other))

    def __ne__(self, other):
        """
        Returns the opposite for the != operator.
        """
        return (not super().__ne__(other))
