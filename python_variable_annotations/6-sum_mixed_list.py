#!/usr/bin/env python3
"""
This module provides a function to calculate
the sum of the elements
of a list of integers and floating-point numbers.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return sum(mxd_lst)
