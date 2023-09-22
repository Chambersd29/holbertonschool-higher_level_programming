#!/usr/bin/python3
def main():

import sys

if len(sys.argv) == 2:
    print("{} argument:".format(len(sys.argv)-1))
elif len(sys.argv) == 1:
    print("{} arguments.".format(len(sys.argv)-1))
else:
    print("{} arguments:".format(i))

for i in range(1, len(sys.argv)):
    argument = sys.argv[i]
    print(f"{i}: {argument}")

if __name__ == "__main__":
    main()
