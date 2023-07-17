#!/usr/bin/python3
"""
This module contains a function that returns
True if the object is an instance of a class
that inherited (directly or indirectly) from
the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Function returns True or False if the object is an
    instance of a class that inherited or not.
    """
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
