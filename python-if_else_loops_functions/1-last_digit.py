#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
lastNumber = int(str(num)[-1:])
if num < 0:
    lastNumber *= -1
if lastNumber > 5:
    print(f"Last digit of {num} is {lastNumber} and is greater than 5")
elif lastNumber == 0:
    print(f"Last digit of {num} is {lastNumber} and is 0")
else:
    print(f"Last digit of {num} is {lastNumber} and is less than 6 and not 0")
