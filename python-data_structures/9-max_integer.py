#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    maxNum = float('-inf')
    for i in range(len(my_list)):
        if my_list[i] > maxNum:
            maxNum = my_list[i]
    return maxNum
