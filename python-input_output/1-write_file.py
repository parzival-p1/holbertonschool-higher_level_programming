#!/usr/bin/python3
"""
This Module contains function that writes a string
to text file and returns number of characters written
"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file (UTF8)
    and returns the number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return (myFile.write(str(text)))
