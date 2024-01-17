#!/usr/bin/python3
""" module contains text_indendation function """


def text_indentation(text):
    """ function to separate and print text at special characters """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    special_chars = ['.', '?', ':']
    parts = []
    for char in special_chars:
        temp_parts = text.split(char)
        if len(temp_parts) > 1:
            parts = temp_parts
            break
    if parts:
        for i in range(len(parts)-1):
            print(parts[i], end="")
            print(char, end="")
            if i != len(parts)-2:
                print("\n")
    else:
        print(text)
