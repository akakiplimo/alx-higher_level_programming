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

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        fileName = cls.__name__ + ".json"
        listObj = []
        if list_objs is not None:
            for i in list_objs:
                listObj.append(cls.to_dictionary(i))
        with open(fileName, "w") as f:
            f.write(cls.to_json_string(listObj))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
