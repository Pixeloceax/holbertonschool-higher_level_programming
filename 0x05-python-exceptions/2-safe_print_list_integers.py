def safe_print_list_integers(my_list=[], x=0):
    for y in range(x):
        try:
            print("{:d}".format(my_list[y]),end='')
            y+=1
        except(IndexError , ValueError):
            continue
    print()
    return(y)