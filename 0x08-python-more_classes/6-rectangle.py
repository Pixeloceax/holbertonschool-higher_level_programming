#!/usr/bin/python3
"""comment"""


class Rectangle:
    """class comment"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        comment
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            comment
        """
        return(self.__width)

    @width.setter
    def width(self, value):
        """
            comment
        """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            comment
        """
        return(self.__height)

    @height.setter
    def height(self, value):
        """
            comment
        """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            comment
        """
        return(self.__width * self.__height)

    def perimeter(self):
        """
            comment
        """
        if self.__width == 0 or self.__height == 0:
            return(0)
        return((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """
            comment
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

    def __repr__(self):
        """
            comment
        """
        tuple = (self.__width, self.__height)
        return("Rectangle{}".format(tuple))

    def __repr__(self):
        """
            comment
        """
        sstr = "Rectangle(" + str(self.__width) + ","
        sstr += str(self.__height) + ")"
        return sstr

    def __del__(self):
        """
            comment
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
