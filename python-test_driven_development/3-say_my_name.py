#!/usr/bin/python3
"""
Este modulo presenta la función say_my_name,
esta función imprime un mensajem el stdout.
"""


def say_my_name(first_name, last_name=""):
    """
    Esta función imprime en la stdout:
    My name is <first name> <last name>

    Args:
        first_name (str): Nombres a imprimir
        last_name (str [opcional]): Apellidos a imprimir.
    Raises:
        TypeError: Sí first_name | last_name != str.
    Return:
        None
    Example:
        >>> say_my_name("John", "Smith")
        >>> My name is John Smith
    """
    full_name = dict(first_name=first_name, last_name=last_name)

    for k, v in full_name.items():
        if not isinstance(v, str):
            raise TypeError(f"{k} must be a string")
    print(f"My name is {first_name} {last_name}")
