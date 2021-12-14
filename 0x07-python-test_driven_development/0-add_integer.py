#!/usr/bin/python3
"""
This 0-add_integer module provides one function add_integer(a,b) e.g.
>>> add_integer(4,6)
10
"""
def add_integer(a, b=98):
    """Returns the sum of 2 integers"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
