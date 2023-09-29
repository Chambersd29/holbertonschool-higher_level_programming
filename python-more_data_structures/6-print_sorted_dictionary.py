#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    new_a = a_dictionary.copy()
    sorted_keys = sorted(new_a.keys())
    for key in sorted_keys:
        print("{}: {}".format(key, new_a[key]))
