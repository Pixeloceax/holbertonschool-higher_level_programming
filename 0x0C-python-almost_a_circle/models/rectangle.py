#!/usr/bin/python3
"""comment"""
from models.base import Base


class Rectangle(Base):
    """comment"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            comment
        """
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            comment
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            comment
        """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise TypeError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
            comment
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            comment
        """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise TypeError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
            comment
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            comment
        """
        if isinstance(value, int) is False:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise TypeError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
            comment
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            comment
        """
        if isinstance(value, int) is False:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise TypeError("y must be >= 0")
        self.__y = value

    def display(self):
        """
            comment
        """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def area(self):
        """
            comment
        """
        return self.__height * self.__width

    def __str__(self):
        """
            comment
        """
        return("[Rectangle] ({}) {}/{} - {}/{}".format
               (self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """
            comment
        """
        rectangle_list = ["id", "width", "height", "x", "y"]
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, rectangle_list[i], args[i])

        elif kwargs is not None:
            for y, value in kwargs.items():
                if y in rectangle_list:
                    setattr(self, y, kwargs[y])

    def to_dictionary(self):
        """
            comment
        """
        rectangle_list = ["id", "width", "height", "x", "y"]
        rectangle_list_self = [self.id, self.width,
                               self.height, self.x, self.y]
        return(dict(zip(rectangle_list, rectangle_list_self)))
