#!/usr/bin/python3
#!/usr/bin/python3
"""module defines read file function"""


def write_file(filename="", text=""):
    """ function to write to file and return number of characters"""
    with open(filename, mode='w', encoding='utf-8') as a_file:
        a_file.write(text)
        num_chars = len(text)
        return num_chars
