#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
An element in the list is said to be peak if
it is NOT smaller than its neighbors.
For corner elements, we need to consider only one neighbor.
"""


def find_peak(list_of_integers):
    """ finds a peak element """
    if list_of_integers == []:
        return None

    def recursive(list_of_integers, left=0, right=len(list_of_integers) - 1):
        """helper recursive function"""

        mid = (left + right) // 2

        # check if the middle element is greater than its neighbors
        if ((mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and
                (mid == len(list_of_integers) - 1 or list_of_integers[mid + 1] <= list_of_integers[mid])):
            return list_of_integers[mid]

        # If the left neighbor of `mid` is greater than the middle element,
        # find the peak recursively in the left sublist
        if mid - 1 >= 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            return recursive(list_of_integers, left, mid - 1)

        # If the right neighbor of `mid` is greater than the middle element,
        # find the peak recursively in the right sublist
        return recursive(list_of_integers, mid + 1, right)

    return recursive(list_of_integers)
    
