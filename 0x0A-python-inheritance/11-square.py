#!/usr/bin/python3
"""comment"""


class BaseGeometry():
    """
        comment
    """
    def area(self):
        """
            comment
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            comment
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""comment"""


class Rectangle(BaseGeometry):
    """
        comment
    """
    def __init__(self, width, height):
        """
            comment
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        """
            comment
        """
        return ("[Rectangle] {:}/{:}".format(self.__height, self.__width))


"""comment"""


class Square(Rectangle):
    """
        comment
    """
    def __init__(self, size):
        """
            comment
        """
        self.__size = size
        super().integer_validator("size", size)

    def area(self):
        """
            comment
        """
        return self.__size * self.__size

    def __str__(self):
        """
            comment
        """
        return ("[Square] {:}/{:}".format(self.__size, self.__size))
