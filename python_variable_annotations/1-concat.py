#!/usr/bin/env python3
"""
This module provides a function to concatenate two strings.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatène deux chaînes de caractères et retourne la chaîne résultante.

    Paramètres :
    str1 (str) : La première chaîne de caractères.
    str2 (str) : La deuxième chaîne de caractères.

    Retourne :
    str : La chaîne résultante de la concaténation de str1 et str2.

    Exemple :
    >>> concat("hello", "world")
    'helloworld'
    """
    return str1 + str2
