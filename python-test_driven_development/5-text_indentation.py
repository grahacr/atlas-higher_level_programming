#!/usr/bin/python3
""" module contains text_indendation function """


def text_indentation(text):
    """ function to separate and print text at special characters """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    special_chars = ['.', '?', ':']
    for char in special_chars:
        parts = text.split(char)
        if len(parts) > 1:
            for i in range(len(parts)-1):
                print(parts[i], end="")
                print(char)
                print("\n\n")
        print(text)
