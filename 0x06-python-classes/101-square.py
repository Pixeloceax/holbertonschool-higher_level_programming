#!/usr/bin/python3
"""Module comment"""


class Square:
    """class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """
            self: instance of the class
            size: size
        """
        self.size = size
        self.position = position

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
    @property
    def position(self):
        """
            self: instance of the class
        """
        return (self.__position)
    """class comment"""
    @position.setter
    def position(self, value):
        """
            self: instance of the class
            value: value
        """
        if isinstance(value, tuple) is False or len(value) != 2 \
           or isinstance(value[0], int) is False or value[0] < 0 \
           or isinstance(value[1], int) is False or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """class comment"""
    def area(self):
        """
            self: instance of the class
        """
        return(self.__size**2)

    """class comment"""
    def my_print(self):
        """
            self: instance of the class
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for k in range(0, self.__size):
                print("#", end="")
            print()
    """class comment"""
    def __str__(self):
        """
            self: instance of the class
        """
        if self.__size != 0:
            for i in range(self.__position[1]):
                print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for k in range(self.__size):
                print("#", end="")
            if i != self.__size - 1:
                print()
        return("")
