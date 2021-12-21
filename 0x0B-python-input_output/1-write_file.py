#!/usr/bin/python3
"""module that defines a function write_file"""


def write_file(filename="", text=""):
    """function that writes a string to a text file in UTF8
    and returns the number of characters written"""    
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
