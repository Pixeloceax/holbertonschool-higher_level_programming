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
        """
        str = ""
        if self.__width != 0 or self.__height != 0:
            str += "\n".join("#" * self.__width for y in range(self.__height))
        return str
    """class comment"""
    def __repr__(self):
        """
            self: instance of the class
        """
        sstr = "Rectangle(" + str(self.__width) + ","
        sstr += str(self.__height) + ")"
        return sstr
    """class comment"""
    def __del__(self):
        """
            self: instance of the class
        """
        print("Bye rectangle...")
