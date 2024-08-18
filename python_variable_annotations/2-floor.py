#!/usr/bin/env python3
"""
This module provides a function to get the lower integer
part of a floating point number.
"""


import math


def floor(n: float) -> int:
    """
    Retourne la partie entière inférieure du nombre flottant donné.

    Paramètre :
    n (float) : Le nombre flottant dont on veut obtenir
    la partie entière inférieure.

    Retourne :
    int : La partie entière inférieure de n.

    Exemple :
    >>> floor(3.14)
    3
    """
    return math.floor(n)
