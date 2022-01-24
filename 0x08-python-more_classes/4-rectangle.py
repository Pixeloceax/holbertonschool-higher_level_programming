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
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
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
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    """class comment"""
    def area(self):
        """
            self: instance of the class
        """
        return(self.__height * self.__width)
    """class comment"""
    def perimeter(self):
        """
            self: instance of the class
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)
    """class comment"""
    def __str__(self):
        """
            self: instance of the class
            S O Colas
        """
        if self.__width == 0 or self.__height == 0:
            return("")
        square = []
        for i in range(self.__height):
            for j in range(self.__width):
                square.append("#")
            if self.__height - 1 != i:
                square.append("\n")
        return("".join(square))
    """class comment"""
    def __repr__(self):
        """
            self: instance of the class
        """
        tuple = (self.__width, self.__height)
        return("Rectangle{}".format(tuple))
