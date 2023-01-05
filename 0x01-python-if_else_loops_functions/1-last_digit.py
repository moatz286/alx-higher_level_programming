#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
boom = 0
if number < 0:
    number *= -1
    boom = 1
lastd = int(repr(number)[-1])
if boom == 1:
    number *= -1
    lastd *= -1
if lastd > 5:
    print(f"Last digit of {number} is {lastd} and is greater than 5")
elif lastd == 0:
    print(f"Last digit of {number} is {lastd} and is 0")
else:
    print(f"Last digit of {number} is {lastd} and is less than 6 and not 0")
