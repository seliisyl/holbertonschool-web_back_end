#!/usr/bin/env python3
"""
This module provides a coroutine to collect 10 random numbers
using an async comprehension over async_generator.
"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension
    over async_generator.

    Returns:
        List[float]: A list containing 10 random float
        numbers generated asynchronously.
    """
    return [number async for number in async_generator()]
