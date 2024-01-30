#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorts = dict(sorted(a_dictionary.items(), key=lambda x: x[0]))
    for k, v in sorts.items():
        print("{}: {}".format(k, v))
