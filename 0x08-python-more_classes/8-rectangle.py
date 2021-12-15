#!/usr/bin/python3
"""
8-rectangle.py
Adrian A. Kiplimo
Module that defines a class Rectangle
"""


class Rectangle:
    """Defines a rectangle with properties"""

    # class attributes
    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __init__(self, width=0, height=0):
        """initializes the rectangle width and height"""
        self.__width = width
        self.__height = height
        
        # increments number of instances by 1 on initialization
        Rectangle.number_of_instances += 1

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
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        struct = []
        for i in range(self.__height):
            [struct.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                struct.append("\n")
        return ("".join(struct))

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle ({:d},{:d})".format(self.__width, self.__height)

    def __del__(self):
        """detroyer which deletes Rectangle instance"""
        print("Bye rectangle...")

        # decrements number of intances by 1 on deletion
        Rectangle.number_of_instances -= 1
