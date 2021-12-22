#!/usr/bin/python3
"""Module that defines class Student"""


class Student:
    """class that represents a Student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation params"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for a in attrs:
            try:
                new_dict[a] = self.__dict__[a]
            except:
                pass
        return new_dict
