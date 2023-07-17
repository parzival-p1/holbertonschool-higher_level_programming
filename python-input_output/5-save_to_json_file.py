#!/usr/bin/python3
import json
"""
This module contains a function that writes an Object to a text file,
using a JSON representation.
"""


def save_to_json_file(my_obj, filename):
    """
    Function that writes an obj to a JSON text file.
    """
    with open(filename, mode="w") as myFile:
        json.dump(my_obj, myFile)
