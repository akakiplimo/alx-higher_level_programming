#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """ finds all multiples of 2 in a list """
    divTwo_list = []

    for i in my_list:
        divTwo_list.append(True) if (my_list[i] % 2) == 0 else divTwo_list.append(False)
    
    return (divTwo_list)
