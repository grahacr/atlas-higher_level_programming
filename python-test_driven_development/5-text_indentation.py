#!/usr/bin/python3
""" """
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    special_chars = ['.', '?', ':']
    for char in special_chars:
        parts = text.split(char)
        for i in range(len(parts)-1):
            print(parts[i], end="")
            print(char)
            print("\n\n")