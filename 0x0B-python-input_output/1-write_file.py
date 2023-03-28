!/usr/bin/python3
"""This module defines a file-writing function."""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(text)
