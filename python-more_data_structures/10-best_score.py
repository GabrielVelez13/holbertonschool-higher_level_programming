#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    highest = float('-inf')
    for key in a_dictionary:
        if a_dictionary[key] > highest:
            highest = a_dictionary[key]
            the_key = key
    return the_key
