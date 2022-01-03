#!/usr/bin/python3
def no_c(my_string):
    C = my_string.translate({ord(i): None for i in 'cC'})
    return C
