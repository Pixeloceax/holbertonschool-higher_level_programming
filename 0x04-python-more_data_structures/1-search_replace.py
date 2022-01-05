#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for idx, search in enumerate(my_list):
        if search == 2:
            my_list[idx] = replace
    print(my_list)
