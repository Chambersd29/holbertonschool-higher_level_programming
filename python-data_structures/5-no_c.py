#!/usr/bin/python3

def no_c(my_string):
    for c in my_string:
        if c != 'c' and c != 'C':
            print(c, end="")

    return ""
