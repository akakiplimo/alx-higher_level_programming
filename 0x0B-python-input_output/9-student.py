#!/usr/bin/python3
"""Module that defines class Student"""


class Student:
    """class that represents a Student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation params"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student"""
        return self.__dict__
