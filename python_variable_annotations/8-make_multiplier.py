#!/usr/bin/env python3
"""
Ce module fournit une fonction pour créer une fonction multiplicatrice.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Prend un float `multiplier` en argument et retourne une fonction
    qui multiplie un float par `multiplier`.

    Paramètres:
    multiplier (float): La valeur du multiplicateur.

    Retourne:
    Callable[[float], float]: Une fonction qui multiplie
    un float par `multiplier`.

    Exemple:
    >>> multiplier_function = make_multiplier(2.22)
    >>> multiplier_function(2.22)
    4.9284
    """
    def multiplier_function(value: float) -> float:
        """
        Multiplie la valeur donnée par le multiplicateur.

        Paramètres:
        value (float): La valeur à multiplier.

        Retourne:
        float: Le résultat de la multiplication.
        """
        return value * multiplier
    return multiplier_function
