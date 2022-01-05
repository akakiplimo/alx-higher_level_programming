#!/usr/bin/python3
"""Module that defines a class Base"""


class Base:
    """ represents a class Base """
    __nb_objects = 0

    def __init__(self, id = None):
        """ class construtor that initializes the class """
        if (id != None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        
    
