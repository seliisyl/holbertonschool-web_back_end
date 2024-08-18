#!/usr/bin/env python3
"""
This module provides a function to calculate
the sum of the elements of a list of integers and floating-point numbers.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calcule la somme des nombres entiers et flottants dans une liste.

    Paramètre :
    mxd_lst (List[Union[int, float]]): Une liste de nombres entiers
    et flottants à additionner.

    Retourne :
    float: La somme des nombres entiers et flottants dans la liste.

    Exemple :
    >>> sum_mxd_lst([5, 4, 3.14, 666, 0.99])
    679.13
    """
    return sum(mxd_lst)
