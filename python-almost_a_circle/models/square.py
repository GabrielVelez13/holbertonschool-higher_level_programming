#!/usr/bin/python3
"""
Square module containing the Square class, a subclass of Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class, a subclass of Rectangle.

    Attributes:
        size (int): The size of the square.

    Methods:
        __init__(self, size, x=0, y=0, id=None):
            Initializes a new instance of the Square class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate. Defaults to 0.
            y (int, optional): The y-coordinate. Defaults to 0.
            id (int, optional): The unique identifier. Defaults to None.
        """
        super().__init__(size, size, x, y, id)
        self.width = size
        self.height = size

    def __str__(self) -> str:
        """ Returns values of the object when __str__ is invoked. """
        return "[Square] ({}) {}/{} - {}" \
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.inputChecker("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Updates rectangle after the fact. """
        if args:
            attributes = ['id', 'size', 'x', 'y']

            for attribute, arg in zip(attributes, args):
                if arg is not None:
                    setattr(self, attribute, arg)

        elif kwargs:
            for attribute, arg in kwargs.items():
                if arg is not None:
                    setattr(self, attribute, arg)

    def to_dictionary(self):
        """ Creates a dictionary of the object. """
        return {"id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y}
