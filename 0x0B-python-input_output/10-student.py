#!/usr/bin/python3
"""comment"""


class Student:

    def __init__(self, first_name, last_name, age):
        """
            comment
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            comment
        """
        self_dict = self.__dict__
        comp = 0

        if type(attrs) == list:
            for i in attrs:
                if type(i) == str:
                    comp += 1
            if len(attrs) == comp:
                j = {}
                for i in self_dict.keys():
                    if i in attrs:
                        j[i] = self_dict[i]
                return j
        else:
            return self_dict
