#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    i = []
    for k in range(list_length):
        try:
            d = my_list_1[k] / my_list_2[k]
        except TypeError:
            print("wrong type")
            d = 0
        except ZeroDivisionError:
            print("division by 0")
            d = 0
        except IndexError:
            print("out of range")
            d = 0
        finally:
            i.append(d)
    return i
