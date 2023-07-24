#!/usr/bin/python3
"""
This modules contains a class Base
with all its methods and attributes
definition
"""
import json
import csv


class Base:
    """
    This class has a private attribute __nb_objects = 0
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiation of class which checks for id. If id is not None
        assign the public instance attribute id with this argument
        otherwise, increment __nb_objects and assign the new value
        to the public instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method that returns the JSON string representation of
        list_dictionaries. If list_dictionaries is None or empty, return
        the string: "[]". Otherwise, return the JSON string representation
        of list_dictionaries.
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class method that writes the JSON string representation of list_objs
        to a file. list_objs is a list of instances who inherits of Base.
        If list_objs is None, save an empty list.
        """
        _file = cls.__name__ + ".json"
        _list = []
        if list_objs is not None:
            for i in list_objs:
                _list.append(cls.to_dictionary(i))
        with open(_file, "w") as myFile:
            myFile.write(cls.to_json_string(_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Static method that returns the list of the JSON string representation.
        If json_string is None or empty, return an empty list.
        Otherwise, return the list represented by json_string.
        """
        if json_string is None or len(json_string) == 0:
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        Class method that returns an instance with all attributes already set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Class method that returns a list of instances. The filename must
        be: <Class name>.json - If the file doesn’t exist, return an empty
        list. Otherwise, return a list of instances.
        """
        fn = cls.__name__ + ".json"
        lst = []
        try:
            with open(fn, mode="r") as myFile:
                lst = cls.from_json_string(myFile.read())
            for i, j in enumerate(lst):
                lst[i] = cls.create(**lst[i])
        except FileNotFoundError:
            pass
        return (lst)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Class method that serializes in CSV.
        """
        fn = cls.__name__ + ".csv"
        if fn == "Rectangle.csv":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]
        with open(fn, mode="w", newline="") as myFile:
            if list_objs is None:
                writer = csv.writer(myFile)
                writer.writerow([[]])
            else:
                writer = csv.DictWriter(myFile, fieldnames=fields)
                writer.writeheader()
                for x in list_objs:
                    writer.writerow(x.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Class method that deserializes in CSV.
        """
        try:
            fn = cls.__name__ + ".csv"
            with open(fn, newline="") as myFile:
                reader = csv.DictReader(myFile)
                lst = []
                for x in reader:
                    for i, n in x.items():
                        x[i] = int(n)
                    lst.append(x)
                return ([cls.create(**objt) for objt in lst])
        except FileNotFoundError:
            return ([])
