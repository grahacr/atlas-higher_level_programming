#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    new = -(abs(number) % 10)
else:
    new = abs(number) % 10
print(f"Last digit of {number} is {new}", end=" ")
if new > 5:
    print("and is greater than 5")
elif new == 0:
    print("and is 0")
elif new < 6:
    print("and is less than 6 and not 0")
