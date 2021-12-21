#!/usr/bin/python3
"""defines a function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """True if an obj is an instance or is inherited from class, else False"""
    return isinstance(obj, a_class)
