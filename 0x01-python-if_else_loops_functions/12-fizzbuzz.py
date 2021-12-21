#!/usr/bin/python3
def fizzbuzz():
    for fizzbuzz in range(1, 101):
        if fizzbuzz % 15 == 0:
            print("fizzbuzz", end=' ')
            continue
        elif fizzbuzz % 3 == 0:
            print("fizz", end=' ')
            continue
        elif fizzbuzz % 5 == 0:
            print("buzz", end=' ')
            continue
        print(fizzbuzz, end=' ')
