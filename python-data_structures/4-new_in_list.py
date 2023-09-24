#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    second_list = my_list.copy()
    if idx < 0:
        return second_list
    elif idx > len(my_list):
        return second_list
    else:
        pass
    for i in range(len(second_list)):
        second_list[idx] = element
        return second_list
