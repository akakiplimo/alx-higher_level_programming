#!/usr/bin/python3
"""Module that defines a class Base"""


import json


class Base:
    """ represents a class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class construtor that initializes the class """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)
