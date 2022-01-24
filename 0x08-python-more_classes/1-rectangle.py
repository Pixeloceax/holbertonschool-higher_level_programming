#!/usr/bin/python3
"""comment"""


class Rectangle:
    """nothing"""
    def __init__(self, width=0, height=0):
        """
            comment
        """
        self.height = height
        self.width = width
    """class comment"""
    @property
    def width(self):
        """
            comment
        """
        return self.__width
    """class comment"""
    @width.setter
    def width(self, value):
        """
            comment
        """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__width = value
    """class comment"""
    @property
    def height(self):
        """
            comment
        """
        return self.__height
    """class comment"""
    @height.setter
    def height(self, value):
        """
            comment
        """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__height = value
