#!/usr/bin/python3
"""Check if two classes are the same """


def is_same_class(obj, a_class):
    """is_same_class

    Args:
        obj: object to check
        a_class: class to check against
    """
    return type(obj) is a_class
