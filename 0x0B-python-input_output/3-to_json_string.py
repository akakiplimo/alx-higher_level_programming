#!/usr/bin/python3
"""defines a function to_json_string"""


import json


def to_json_string(my_obj):
    """function that returns the JSON representation of obj(string)"""
    return json.dumps(my_obj)
