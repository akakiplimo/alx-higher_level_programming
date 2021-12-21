#!/usr/bin/python3
"""module that defines a function append_write"""


def append_write(filename="", text=""):
    """function that appends a string to the end of a text
    file in UTF8 and returns the number of characters added"""

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
