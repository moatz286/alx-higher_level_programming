#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
boom = 0
if number < 0:
    number *= -1
    boom = 1
last_digit = int(repr(number)[-1])
if boom == 1:
    number *= -1
    last_digit *= -1
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit}  and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit}  and is zero")
else:
     print(f"Last digit of {number} is {last_digit}  and is less than 6 and not 0")