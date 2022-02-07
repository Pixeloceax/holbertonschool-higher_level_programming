#!/usr/bin/python3
"""module to print a Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        comment
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            comment
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
            comment
        """
        return("[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """
            comment
        """
        return(self.width)

    @size.setter
    def size(self, size):
        """
            comment
        """
        self.height = size
        self.width = size

    def update(self, *args, **kwargs):
        """
            comment
        """
        rectangle_list = ["id", "size", "x", "y"]
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, rectangle_list[i], args[i])

        elif kwargs is not None:
            for y, size in kwargs.items():
                if y in rectangle_list:
                    setattr(self, y, kwargs[y])

    def to_dictionary(self):
        """
            comment
        """
        square_list = ["id", "size", "x", "y"]
        square_list_self = [self.id, self.size, self.x, self.y]
        return(dict(zip(square_list, square_list_self)))
