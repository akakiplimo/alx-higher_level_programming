#!/usr/bin/python3
"""
4-rectangle.py
Adrian A. Kiplimo
Module that defines a class Rectangle
"""


class Rectangle:
    """Defines a rectangle with properties"""
    def __init__(self, width=0, height=0):
        """initializes the rectangle width and height"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the rectangle perimeter"""
        return ((self.__width * 2)+(self.__height * 2))

    def __str__(self):
        """returns a string representation of the string that is printable with #"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width for j in range(self.__height))
        return string

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle ({:d},{:d})".format(self.__width, self.__height)
