#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    def mult_num(tuple):
        fact1, fact2 = tuple
        return fact1 * fact2
    return list(map(mult_num, [(x, number) for x in my_list]))
