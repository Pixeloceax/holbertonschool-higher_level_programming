#!/usr/bin/python3
def print_arg(argv):
    numbers = len(argv) - 1
    if numbers == 0:
        print("{0} argument.".format(numbers))
        return
    else:
        if numbers == 1:
            print("{0} argument:".format(numbers))
        else:
            print("{0} arguments:".format(numbers))
        a = 1
        while a <= numbers:
            print("{0}: {1}".format(a, argv[a]))
            a += 1


if __name__ == "__main__":
    import sys
    print_arg(sys.argv)
