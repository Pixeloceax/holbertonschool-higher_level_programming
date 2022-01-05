#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_key = max(a_dictionary, key=a_dictionary.get)
    if max_key in a_dictionary:
        return max_key
