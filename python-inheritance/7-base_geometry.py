#!/usr/bin/python3
""" Defines geometry class"""


class BaseGeometry:
    """ Base Geometry """

    def area(self):
        """ Exception for now """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates interger"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
