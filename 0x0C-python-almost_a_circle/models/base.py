#!/usr/bin/python3
"""comment"""


import json

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """
            comment
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects +=1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
            comment
        """
        if list_dictionaries is None or len(list_dictionaries) ==0:
            return "[]"
        return json.dumps(list_dictionaries)


    def save_to_file(cls, list_objs):
        """
            commment
        """
        if list_objs is None:
            