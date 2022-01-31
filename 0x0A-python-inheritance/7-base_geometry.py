#!/usr/bin/python3
"""comment"""


class BaseGeometry:
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
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
    