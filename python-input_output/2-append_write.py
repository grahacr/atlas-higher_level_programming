#!/usr/bin/python3
""" module defines read file function"""


def append_write(filename="", text=""):
    """ function to apend text to file and return number of characters"""
    with open(filename, mode='a', encoding='utf-8') as a_file:
        a_file.write(text)
        num_chars = len(text)
        return num_chars
