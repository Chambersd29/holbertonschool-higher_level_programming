#!/usr/bin/python3
"""
    define la función matrix
"""

def matrix_divided(matrix, div):
    """
    esta funcion debe recibir una lista de lista con int o float,
    debe divir cada elemtno entre div y regresar una lista nueva.
    cada elemento redondeado a 2 decimales.
    
    Args:
        matrix([[]]): Matrix es una lista de lista con int o float.
        div (int || float): Será el divisor de cada item dentro matrix.

    Raises:
        TypeError: Si matrix no es lista de lista con int o float.
        TypeError (len(matrix[i])): si cada lista interna tiene un tamaño distinto.
        TypeError (div !=int | float): Si div no es un int o float
        ZeroDivisionError (div == 0): si div es 0.
    Returns:
    new_list ([[]])
    """

    MSG_TYPERROR_LIST = "matrix must be a matrix (list of lists)" \
                        " of integers/floats"
    MSG_ERROR_SIZE_LIST = "Each row of the matrix must have the same size"
    MSG_TYPERROR_DIV = "div must be a number"
    MSG_ZEROERROR_DIV = "division by zero"

    # Crea una lista para agregando el tipo de cada intem y matrix
    is_list_of_list = [isinstance(m, list)
                       for m in matrix] + [isinstance(matrix, list)]

    # Comprueba que todos que matrix sea una lista, y cada  item tbm lo sea.
    if not all(is_list_of_list):
        raise TypeError(MSG_TYPERROR_LIST)

    if all([len(m) == 0 for m in matrix]):
        raise TypeError(MSG_TYPERROR_LIST)

    # Comprueba que cada item dentro de la lista de lista sea un int u float.
    if not all([all([isinstance(i, (int, float)) for i in m])for m in matrix]):
        raise TypeError(MSG_TYPERROR_LIST)

    # Comprueba que cada lista dentro de lista tenga el mismo tamaño.
    if len(set([len(m) for m in matrix])) != 1:
        raise TypeError(MSG_ERROR_SIZE_LIST)

    # Comprueba que div sea un int o float.
    if not isinstance(div, (int, float)):
        raise TypeError(MSG_TYPERROR_DIV)

    # Comprueba que div == 0.
    if div == 0:
        raise ZeroDivisionError(MSG_ZEROERROR_DIV)

    return [[round(n/div, 2) for n in m] for m in matrix]
