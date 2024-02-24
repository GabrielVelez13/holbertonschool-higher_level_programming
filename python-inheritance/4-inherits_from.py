#!/usr/bin/python3
"""inherits_from"""


def inherits_from(obj, a_class):
    """inherits_from

    Args:
        obj: object to check
        a_class: class to check against
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
