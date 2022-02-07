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
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            comment
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            comment
        """

        fname = cls.__name__ + ".json"
        lista = []
        with open(fname, mode='w', encoding='utf-8') as a_file:
            if list_objs is None:
                a_file.write(cls.to_json_string([]))
            else:
                for obj in list_objs:
                    lista.append(obj.to_dictionary())
                a_file.write(cls.to_json_string(lista))

    @staticmethod
    def from_json_string(json_string):
        """
            comment
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            comment
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                create = cls(1, 1)
            else:
                create = cls(1)
            create.update(**dictionary)
            return create

    @classmethod
    def load_from_file(cls):
        """
            comment
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
