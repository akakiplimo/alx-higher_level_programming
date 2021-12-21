#!/usr/bin/python3
"""Defines MyList Class"""


class MyList(list):
    """A subclass of list"""
    def __init__(self):
        """initializes the list"""
        super().__init__()

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
