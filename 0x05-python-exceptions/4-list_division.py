#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    y = 0
    sum_list = []
    for y in range(list_length):
        try:
            sum = my_list_1[y] / my_list_2[y]
        except(TypeError):
            print("wrong type")
            sum = 0
        except(IndexError):
            print("out of range")
            sum = 0
        except(ZeroDivisionError):
            print("division by 0")
            sum = 0
        finally:
            sum_list.append(sum)
    return sum_list
