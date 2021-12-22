#!/usr/bin/python3
"""defines a function load_from_json_file"""


import json


def load_from_json_file(filename):
    """function that creates an Object from JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
