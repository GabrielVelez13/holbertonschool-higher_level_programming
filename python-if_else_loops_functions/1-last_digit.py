#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
lastNum = int(str(num)[-1:])
if num < 0:
    lastNum *= -1
if lastNum > 5:
    print("Last digit of {} is {} and is greater than 5".format(num, lastNum))
elif lastNum == 0:
    print("Last digit of {} is {} and is 0".format(num, lastNum))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(num, lastNum))
