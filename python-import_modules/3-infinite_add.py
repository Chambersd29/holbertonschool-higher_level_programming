#!/usr/bin/python3

import sys
def main():
    u = 0
    arg = len(sys.argv)
    for i in range(arg):
        if i == arg:
            break
    for k in range(1, i + 1):
        u += int(sys.argv[k])
    print(u)
if __name__ == "__main__":
    main()
