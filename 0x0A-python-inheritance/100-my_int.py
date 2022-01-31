#!/usr/bin/python3
"""comment"""


class MyInt(int):
    """
        comment
    """
    def __init__(self, value):
        """
            comment
        """
        self.numbers = value

    def __eq__(self, value1):
        """
            comment
        """
        return self.numbers != value1

    def __ne__(self, value2):
        """
            comment
        """
        return self.numbers == value2
