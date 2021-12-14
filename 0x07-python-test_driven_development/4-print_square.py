#!/usr/bin/python3
"""
This is a module with one funcion print_square(size)
"""
def print_square(size):
    """This is a funciton that prints a square with the character #"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print(("#" * size + "\n") * size, end="")
