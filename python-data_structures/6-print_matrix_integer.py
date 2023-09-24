#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
        return
    list_plane = []
    c = 0
    
    for fila in matrix:
        for elemento in fila:
            list_plane.append(elemento)
    for i in list_plane:
        c += 1
        if c == 3:
            c = 0
            print("{:d}".format(i))
        elif c < 3:
             print("{:d}".format(i), end=" ")
        else:
            pass
