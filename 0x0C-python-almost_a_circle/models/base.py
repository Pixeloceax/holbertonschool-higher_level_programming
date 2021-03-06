#!/usr/bin/python3
"""comment"""
import json
import csv


class Base:
    """comment"""
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
            comment
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
    
    @classmethod
    def load_from_file_csv(cls):
        """
            comment
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
