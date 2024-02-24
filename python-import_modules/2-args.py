#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    numArgs = len(argv) - 1
    if numArgs == 0:
        print("0 arguments.")
    elif numArgs == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(numArgs))
    for i in range(numArgs):
        print("{}: {}".format(i + 1, argv[i + 1]))
