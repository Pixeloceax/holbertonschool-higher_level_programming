#!/usr/bin/python3
"""Module comment"""


class Square:
    """class Square"""
    def __init__(self, size=0):
        """
            self: instance of the class
            size: size
        """
        self.size = size
    """class comment"""
    def area(self):
        """
            self: instance of the class
        """
        return(self.__size**2)
    """class comment"""
    @property
    def size(self):
        """
            self: instance of the class
        """
        return self.__size

    """class comment"""
    @size.setter
    def size(self, value):
        """
            self: instance of the class
            value: value
        """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """class comment"""
    def my_print(self):
        
        print("#", end="")
        if self.__size < 0:
            print()
