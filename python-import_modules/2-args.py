#!/usr/bin/python3
import sys


def print_args():
    count = len(sys.argv) - 1

    if count == 0:
        print("0 arguments.")
        return
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    # list each argument
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))


if __name__ == "__main__":
    print_args()
