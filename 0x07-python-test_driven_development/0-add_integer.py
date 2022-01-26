#!/usr/bin/python3
""" add_ integer """
def add_integer(a, b=98):
    """
        comment
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, (int, bool)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, bool)):
        raise TypeError("b must be an integer")
    return (a + b)