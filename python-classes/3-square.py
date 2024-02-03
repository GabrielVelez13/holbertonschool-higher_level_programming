#!/usr/bin/python3
"""Define the Square class."""


class Square:
    """Represents a square.

    Initializes a new Square with a specified size.
    """
    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
