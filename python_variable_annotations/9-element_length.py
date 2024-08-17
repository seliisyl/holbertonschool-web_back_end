#!/usr/bin/env python3
"""
This module provides a function to get
the length of elements in an iterable.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(
    lst: Iterable[Sequence]
) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples,
    where each tuple contains a sequence and an integer representing
    the length of that sequence.

    Parameters:
    lst (Iterable[Sequence]): An iterable of sequences.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples, each
    containing a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
