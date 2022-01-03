#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    sum = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] % 2:
            sum[i] = False
        else:
            sum[i] = True
    return sum
