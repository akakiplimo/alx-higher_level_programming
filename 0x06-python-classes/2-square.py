#!/usr/bin/python3

"""Defines a class Square"""


class Square:
    """
    Represents a square
    """
    def __init__(self, size=0):
        """size - initialize size attribute of the square"""
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
