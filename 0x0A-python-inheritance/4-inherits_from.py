#!/usr/bin/python3
"""defines a function inherits_from"""


def inherits_from(obj, a_class):
    """True if obj of a subclass of a_class"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
