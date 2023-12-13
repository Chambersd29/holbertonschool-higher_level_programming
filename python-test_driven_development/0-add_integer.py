#!/usr/bin/python3
"""
Este módulo contiene operaciones matemáticas

Example:
    add_integer(4, 9)
"""


def add_integer(a, b=98):
    """
    Esta función suma dos enteros.

    Args:
        a (int): Primer entero
        b (int): Segundo entero(valor por defecto 98)

    Returns:
        int: return a + b
    """
    n = dict(a=a, b=b)

    for k, v in n.items():
        if not isinstance(v, (int, float)):
            raise TypeError(f"{k} must be an integer")
    return int(a) + int(b)
