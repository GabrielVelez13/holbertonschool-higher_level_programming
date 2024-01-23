#!/usr/bin/python3
def print_last_digit(number):
    newNumber = int(str(number)[-1:])
    print(newNumber, end="")
    return newNumber
