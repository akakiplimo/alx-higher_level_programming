#!/usr/bin/python3
""" class Rectangle which inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """instantiated class Rectangle"""
    def __init__(self, width, height):
        """instantiated and validated params"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """calculates area = width * height"""
        return (self.__width * self.__height)

    def __str__(self):
        """str method that prints rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
