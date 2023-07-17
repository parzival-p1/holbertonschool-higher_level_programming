#!/usr/bin/python3
"""
This module contains a function that appends a string at the end
of a text file (UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Returns the number of chars appended to filename from text
    """
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
