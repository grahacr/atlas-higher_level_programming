#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            upper_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            upper_char = char
        upper_str += upper_char
print("{}".format(upper_str))
