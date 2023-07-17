#!/usr/bin/python3
"""
This file contains a function to print
text file to stdout without import.
"""


def read_file(filename=""):
    """
    This function reads a text file and prints it stdout.
    You must use the with statement and don’t need to manage
    file permission or file doesn't exist exceptions.
    """
    with open(filename, encoding="utf-8") as myFile:
        for line in myFile:
            print(line, end="")
