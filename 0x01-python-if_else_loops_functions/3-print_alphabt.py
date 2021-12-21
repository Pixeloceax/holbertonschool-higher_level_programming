#!/usr/bin/python3
def lowercaseAlphabets():
    for c in range(97, 123):
        if c in [101, 113]:
            continue
        print(chr(c), end="")


lowercaseAlphabets()
