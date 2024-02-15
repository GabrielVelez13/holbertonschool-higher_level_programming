#!/usr/bin/python3
"""This is the base of all models to come"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inherits from Base class and
    represents a rectangle in a 2D space.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the top-left corner of the rectangle.
        y (int): The y-coordinate of the top-left corner of the rectangle.
        id (int): The unique identifier for the rectangle.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
            Initializes a new instance of the Rectangle class.

        Getter and setter methods for width, height, x, and y attributes.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the top-left corner
                               of the rectangle. Defaults to 0.
            y (int, optional): The y-coordinate of the top-left corner
                               of the rectangle. Defaults to 0.
            id (int, optional): The unique identifier for the rectangle.
                                Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def inputChecker(self, name: str, input: object, xory=False):
        """ Checks if the input is correct. """
        if not isinstance(input, int):
            raise TypeError("{} must be integer".format(name))
        if not xory:
            if input <= 0:
                raise ValueError("{} must be >= 0".format(name))
        elif input < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value: int):
        """
        Setter method for the width attribute.

        Args:
            value (int): The new value for the width of the rectangle.
        """
        self.inputChecker("width", value)
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value: int):
        """
        Setter method for the height attribute.

        Args:
            value (int): The new value for the height of the rectangle.
        """
        self.inputChecker("height", value)
        self.__height = value

    @property
    def x(self):
        """int: The x-coordinate of the top-left corner of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value: int):
        """
        Setter method for the x attribute.

        Args:
            value (int): The new value for the x-coordinate of the rectangle.
        """
        self.inputChecker("x", value, True)
        self.__x = value

    @property
    def y(self):
        """int: The y-coordinate of the top-left corner of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value: int):
        """
        Setter method for the y attribute.

        Args:
            value (int): The new value for the y-coordinate of the rectangle.
        """
        self.inputChecker("y", value, True)
        self.__y = value
