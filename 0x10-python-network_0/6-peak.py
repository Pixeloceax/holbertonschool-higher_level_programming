#!/usr/bin/python3
"""
Find a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers
    """
    if not list_of_integers:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        return ((list_of_integers[0], list_of_integers[1])
                [list_of_integers[0] < list_of_integers[1]])


    if list_of_integers[int((len(list_of_integers) - 1) / 2)] < list_of_integers[int((len(list_of_integers) - 1) / 2) + 1]:
        return find_peak(list_of_integers[int((len(list_of_integers) - 1) / 2) + 1:])
    else:
        return find_peak(list_of_integers[:int((len(list_of_integers) - 1) / 2) + 1])