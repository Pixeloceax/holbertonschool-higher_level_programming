#!/usr/bin/python3
"""comment"""


def text_indentation(text):
    """
        comment
    """
    cut = 0
    if text[0] == ' ':
        cut = 1
    for index in range(len(text)):
        if text[index] in ['.', '?', ':']:
            print(text[index], end="")
            print('\n')
            cut = 1
        else:
            if cut == 0:
                print(text[index], end="")
            elif cut == 1 and text[index] == ' ':
                continue
            else:
                print(text[index], end="")
                cut = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
