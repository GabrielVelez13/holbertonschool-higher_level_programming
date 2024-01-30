#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0
    Nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    rList = [Nums[x] for x in list(roman_string)]
    total = 0
    idx = 0

    for i in rList:
        if idx != len(rList) - 1 and rList[idx] < rList[idx + 1]:
            total -= i
        else:
            total += i
        idx += 1

    return total
