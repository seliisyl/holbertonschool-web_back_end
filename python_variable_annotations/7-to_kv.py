#!/usr/bin/env python3
"""
This module provides a function to create a tuple
from a string and a number,
where the number is squared.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, float(v ** 2))
