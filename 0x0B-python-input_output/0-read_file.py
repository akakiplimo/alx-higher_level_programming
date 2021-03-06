#!/usr/bin/python3
"""Module that defines a module read_file"""


def read_file(filename=""):
    """function that reads a text file with UTF8 encoding and prints it"""

    with open(filename, encoding="UTF8") as f:
        read_file = f.read()
        print(read_file, end="")
