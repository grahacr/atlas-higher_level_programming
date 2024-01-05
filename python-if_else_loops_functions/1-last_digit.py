#!/usr/bin/python3
import random
number = random.randint(-10, 10)
string = str(number)
last_digit = int(string[-1])
if last_digit > 5:
    print(f"Last digit of {string} is {last_digit} and is greater than 5")
if last_digit == 0:
    print(f"Last digit of {string} is {last_digit} and is 0")
if last_digit != 0 and last_digit < 6:
    print(f"Last digit of {string} is {last_digit} and is less than 6 and not 0")
