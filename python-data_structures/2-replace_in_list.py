#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    else:
        pass
    if my_list[idx] in my_list:
        my_list[idx] = element
        return my_list
