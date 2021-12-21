#!/usr/bin/python3
"""Imports class BaseGeometry and subclass Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representation of a Square with instantiation and area method"""
    def __init__(self, size):
        """instantiation method"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """method that calculates area"""
        return (self.__size ** 2)

    def __str__(self):
        """prints square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
