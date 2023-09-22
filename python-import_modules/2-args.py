#!/usr/bin/python3
import sys

arg = len(sys.argv)
for i in range(arg):
    if i == arg:
        break
if i == 1:
    print("{:d} argument:".format(i))
elif i == 0:
    print("{:d} arguments.".format(i))
else:
    print("{:d} arguments:".format(i))

for i in range(1, len(sys.argv)):
    argument = sys.argv[i]
    print(f"{i}: {argument}")
