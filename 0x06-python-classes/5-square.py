#!/usr/bin/python3
"""Module comment"""
class Square:
    """class comment"""
    def __init__(self, size = 0):

        if isinstance(size, int) == False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """class comment"""
    def area(self):
        return(self.__size**2)

    """class comment"""
    @property
    def size(self):
        return self.__size

    """class comment"""
    @size.setter
    def size(self, value): 
        if isinstance(value, int) == False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        
        print("#", end="")
        if self.__size < 0:
            print()
