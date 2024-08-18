#!/usr/bin/env python3
"""
This module provides a function to calculate
the sum of the elements of a list of floating-point numbers.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of floating-point numbers in a list.

    Parameters:
    input_list (List[float]): A list of floating-point numbers to sum.

    Returns:
    float: The sum of the floating-point numbers in the list.

    Example:
    >>> sum_list([3.14, 1.11, 2.22])
    6.47
    """
    return sum(input_list)
