#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    list = dir()
    for i in (list):
        if i[0] != '_' and i[1] != '_':
            print(i)
