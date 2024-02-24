#!/usr/bin/python3
def uniq_add(my_list=[]):
    repeats = []
    total = 0
    for i in my_list:
        if i not in repeats:
            total += i
            repeats.append(i)
    return total
