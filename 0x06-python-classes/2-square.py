#!/usr/bin/python3
"""Module comment"""


class Square:
    """class Square"""
    def __init__(self, size=0):
        """
            self: instance of the class
            size: size
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
