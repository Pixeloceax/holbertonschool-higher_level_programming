#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    int_check = 1
    for y in range(x):
        if type(my_list[y]) == type(int_check):
            try:
                print("{:d}".format(my_list[y]), end='')
                y += 1
            except(ValueError, TypeError):
                break
        else:
            exit
    print()
    return(y-1)
