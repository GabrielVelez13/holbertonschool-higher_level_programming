#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    total = 0
    numArgs = len(argv) - 1
    for i in range(numArgs):
        total += int(argv[i + 1])
    print(total)
