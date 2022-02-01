#!/usr/bin/python3
def append_write(filename="", text=""):
    """
        comment
    """
    with open(filename, 'a') as f:
        return f.write(text)
