#!/usr/bin/python3
"""This is the base of all models to come"""

import json
from types import MethodType


class Base:
    """
    Base class for objects with an optional identifier.

    Attributes:
        __nb_objects (int): Counts the number of instances created.
        id (int): An identifier for each instance. Automatically
                  assigned if not provided.

    Methods:
        __init__(self, id=None): Initializes a Base instance
                                 with an optional ID.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance.

        Parameters:
            id (int, optional): An optional identifier. Automatically
                                assigned if not provided.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Creates a JSON representation of a dictionary. """
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Saving JSON data of objects to file. """
        title = cls.__name__ + ".json"
        data = []
        if list_objs is not None:
            for obj in list_objs:
                data.append(obj.to_dictionary())
        with open(title, mode="w") as f:
            return f.write(Base.to_json_string(data))

    @staticmethod
    def from_json_string(json_string):
        """ Changing json to dictionary. """
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
