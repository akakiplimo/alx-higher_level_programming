#!/usr/bin/python3
def common_elements(set_1, set_2):
    """ returns a set of common elements in two sets """
    common_list = []
    for i in set_1:
        for j in set_2:
            if i == j:
                common_list.append(i)
    
    return (common_list)
