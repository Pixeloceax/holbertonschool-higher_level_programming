#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
        numbers1 = len(tuple_a)
        numbers2 = len(tuple_b)
        if numbers1 == 0 and numbers2 == 0:
            tuple = (0, 0)
        elif numbers1 == 1 and numbers2 == 1:
            tuple = (tuple_a[0] + tuple_b[0], 0)
        elif numbers1 == 1 and numbers2 != 0:
            tuple = (tuple_a[0] + tuple_b[0], tuple_b[1])
        elif numbers2 == 0 and numbers1 != 0:
            tuple = (tuple_a[0], tuple_a[1])
        elif numbers2 == 1 and numbers1 != 0:
            tuple = (tuple_b[0] + tuple_a[0], tuple_a[1])
        elif numbers1 == 0 and numbers2 != 0:
            tuple = (tuple_b[0], tuple_b[1])
        else:
            tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return tuple

