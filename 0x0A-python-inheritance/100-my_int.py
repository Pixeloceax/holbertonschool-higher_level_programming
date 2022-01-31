#!/usr/bin/python3
class MyInt(int):
    def __init__(self, value):
        self.numbers = value
    def __eq__(self, value1):
        return self.numbers != value1
    def __ne__(self, value2):
        return self.numbers == value2