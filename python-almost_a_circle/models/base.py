#!/usr/bin/python3
"""Creating the base of the project"""


class Base:
    """
    The Base class represents a base object with an optional ID.

    Attributes:
        __nb_objects (int): A class variable to keep track of the number of instances created.
        id (int): An identifier for each instance. If not provided during initialization,
                  it is automatically assigned based on the number of instances created.

    Methods:
        __init__(self, id=None): Initializes a Base instance with an optional ID.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance.

        Parameters:
            id (int, optional): An optional identifier for the instance.
                If not provided, a unique ID is assigned based on the number of instances created.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
