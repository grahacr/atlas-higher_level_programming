#!/usr/bin/python3
"""module defines read file function"""


def read_file(filename=""):
    """ function to open file and print it"""
    with open(filename, encoding='utf-8') as a_file:
        print(a_file.read(), end="")
