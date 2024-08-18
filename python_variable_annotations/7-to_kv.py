#!/usr/bin/env python3
"""
Ce module fournit une fonction pour créer un tuple à partir
d'une chaîne de caractères et d'un nombre, où le nombre est
au carré.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Prend une chaîne de caractères et un nombre (entier ou flottant),
    et retourne un tuple où le nombre est au carré.

    Paramètres :
    k (str): La chaîne de caractères.
    v (Union[int, float]): Le nombre à mettre au carré.

    Retourne :
    Tuple[str, float]: Un tuple avec la chaîne de caractères
    et le carré du nombre.

    Exemple :
    >>> to_kv("eggs", 3)
    ('eggs', 9.0)
    >>> to_kv("school", 0.02)
    ('school', 0.0004)
    """
    return (k, float(v ** 2))
