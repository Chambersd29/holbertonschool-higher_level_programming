#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    diferencia_1 = set_1.difference(set_2)
    diferencia_2 = set_2.difference(set_1)
    diff = diferencia_1.union(diferencia_2)
    return (diff)
