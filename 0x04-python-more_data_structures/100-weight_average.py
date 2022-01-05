#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return (0)
    sum = 0
    sum2 = 0
    for x, y in my_list:
        sum += x * y
        sum2 += y
    return (sum / sum2)
