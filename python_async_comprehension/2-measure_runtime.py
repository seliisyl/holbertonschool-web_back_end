#!/usr/bin/env python3
"""
This module provides a coroutine to measure the runtime
of executing async_comprehension four times in parallel.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing async_comprehension
    four times in parallel.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
