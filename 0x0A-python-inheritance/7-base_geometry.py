#!/usr/bin/python3
"""defines a class BaseGeometry"""


class BaseGeometry:
    """a class with public instance methods area & integer_validator"""
    def area(self):
        """raises an exception with a message"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """validates value"""
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
