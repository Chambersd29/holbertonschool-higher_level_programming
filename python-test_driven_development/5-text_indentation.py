#!/usr/bin/python3
"""
Este módulo expone la siguiente función:
text_indentation
"""


def text_indentation(text):
    """
    Esta función: Imprime un texto con 2
    líneas nuevas después de cada uno de estos
    caracteres: ., ? y :

    Args:
        text (str): Texto a imprimir.
    Returns:
        None
    Example:
        >>> text_indentation("hola.mundo?adios:")
        hola.
        <BLANKLINE>
        mundo?
        <BLANKLINE>
        adios:
        <BLANKLINE>
    """
    character = [(".", ".\n\n"), ("?", "?\n\n"),
                 (":", ":\n\n"), ("\n\n ", "\n\n")]

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = " ".join(text.split())

    for i in character:
        text = text.replace(i[0], i[1])
    print(text, end="")
