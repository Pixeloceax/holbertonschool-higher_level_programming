#!/usr/bin/python3
"""comment"""



from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            comment
        """
        super().__init__(id, width, height, x, y)
        size = height
    def __str__(self):
        """
            comment
        """
        return("[Square] ({}) {}/{} - {}/{}".format
        (self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs): 
        """
            comment
        """
        rectangle_list = ["id", "width", "height", "x", "y"]
        if args is not None and len(args) != 0:
            for i in range (len(args)):
                setattr(self, rectangle_list[i], args[i])

        elif kwargs is not None:
            for y, Value in kwargs.items():
                if y in rectangle_list:
                    setattr(self, y, kwargs[y])
