#!/usr/bin/python3
"""comment"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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

    def __str__(self):
        """
            comment
        """
        return("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))

    def area(self):
        """
            comment
        """
        return(self.__width * self.__height)
