#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    y = int_check = 0
    while True:
        try:
            if y < x:
                print("{:d}".format(my_list[y]), end='')       
                y += 1
                int_check += 1
            else:
                print()
                return int_check
        except (ValueError, TypeError):
            y += 1
