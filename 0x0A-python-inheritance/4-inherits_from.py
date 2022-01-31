#!/usr/bin/python3
"""comment"""


def inherits_from(obj, a_class):
    """
        comment
    """
    return type(obj) != a_class and isinstance(obj, a_class)
