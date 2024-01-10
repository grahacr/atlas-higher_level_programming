#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("The number is {:d}".format(num))
        return True
    except ValueError:
        return False
