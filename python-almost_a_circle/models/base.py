#!/usr/bin/python3
"""This is the base of all models to come"""


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
        if not list_dictionaries:
            return "[]"
        else:
            return "{}".format(list_dictionaries)
