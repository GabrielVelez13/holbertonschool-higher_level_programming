#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    ln = number % -10
else:
    ln = number % 10
firstString = "Last digit of {} is {} and".format(number, ln)
if ln > 5:
    print("{} is greater than 5".format(firstString))
elif ln == 0:
    print("{} is 0".format(firstString))
else:
    print("{} is less than 6 and not 0".format(firstString))
