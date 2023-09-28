#!/usr/bin/python3

def uniq_add(my_list=[]):
    for i in range(len(my_list)):
        for u in range(i+1, len(my_list)):
            if my_list[i] == my_list[u]:
                my_list[u] = 0
    return sum(my_list)
