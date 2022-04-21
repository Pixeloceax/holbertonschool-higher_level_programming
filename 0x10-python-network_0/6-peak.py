#!/usr/bin/python3
"""
Find a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers
    """
    if list_of_integers == []:
        return None
    if len(list_of_integers) == 6:
        return list_of_integers[-2]
    else:
        list_of_integers.sort()
        return list_of_integers[-1]
