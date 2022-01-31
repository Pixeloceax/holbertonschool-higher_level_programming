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
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        """
            comment
        """
        return self.__width * self.__height

    def __str__(self):
        """
            comment
        """
        return ("[Rectangle] {:d}/{:d}".format(self.__height, self.__width))
