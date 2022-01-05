#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    list = a_dictionary.copy()
    for i in list.keys():
        list[i] *= 2
    return list
