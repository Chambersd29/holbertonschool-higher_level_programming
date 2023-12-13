#!/usr/bin/python3
"""
Este módulo define la función
print_square, que imprime en la stdout
un cuadrado.
"""


def print_square(size):
    """
    Esta función imprime en la stdout un cuadrado
    usando como simbolo el '#', del tamaño de size.
    Args:
        size (int): Tamano del cuadrado.
    Returns:
        None
    Example:
        >>> print_square(2)
        ##
        ##
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print("".join([f"{'#' * size}\n" for i in range(size)])[:-1])
