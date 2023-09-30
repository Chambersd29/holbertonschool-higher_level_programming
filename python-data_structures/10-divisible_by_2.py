#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = []
    for num in my_list:
        if num % 2 == 0:
            num = True
            new_list.append(num)
        else:
            num = False
            new_list.append(num)

    return new_list
