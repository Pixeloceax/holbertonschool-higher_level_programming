#!/usr/bin/python3
from typing import Counter


def divisible_by_2(my_list=[]):
    sum = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            sum.append(True)
        else:
            sum.append(False)
        return sum
