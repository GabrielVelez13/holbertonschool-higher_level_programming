#!/usr/bin/python3
""" Module for inheritance of list """


class MyList(list):
    """ Inherits MyList attributes """

    def print_sorted(self):
        """ Prints sorted list """
        issubclass(MyList, list)
        print(sorted(self))
