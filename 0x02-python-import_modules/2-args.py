#!/usr/bin/python3
def print_arg(argv):
    numbers = len(argv) - 1
    if numbers == 0:
        print("{:d} argument.".format(numbers))
        return
    else:
        if numbers == 1:
            print("{:d}} argument:".format(numbers))
        else:
            print("{:d} arguments:".format(numbers))
        a = 1
        while a <= numbers:
            print("{:d}: {:d}".format(a, argv[a]))
            a += 1


if __name__ == "__main__":
    import sys
    print_arg(sys.argv)
