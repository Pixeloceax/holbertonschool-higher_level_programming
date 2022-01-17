#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        sum = a/b
        print("Inside result: {}".format(sum))
    except(ZeroDivisionError):
        sum = None
        print("Inside result: {}".format(sum))
    finally:
        return sum
