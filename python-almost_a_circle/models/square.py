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
