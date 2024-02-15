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

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Args:
            value (int): The new value for the width of the rectangle.
        """
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Args:
            value (int): The new value for the height of the rectangle.
        """
        self.__height = value

    @property
    def x(self):
        """int: The x-coordinate of the top-left corner of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for the x attribute.

        Args:
            value (int): The new value for the x-coordinate of the rectangle.
        """
        self.__x = value

    @property
    def y(self):
        """int: The y-coordinate of the top-left corner of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for the y attribute.

        Args:
            value (int): The new value for the y-coordinate of the rectangle.
        """
        self.__y = value
