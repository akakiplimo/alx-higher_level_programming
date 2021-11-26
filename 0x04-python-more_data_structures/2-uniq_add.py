#!/usr/bin/python3

def uniq_add(my_list=[]):
    """adds all unique integers in a list"""
    sum_uniq = 0
    for i in set(my_list):
        sum_uniq += i
    return (sum_uniq)
