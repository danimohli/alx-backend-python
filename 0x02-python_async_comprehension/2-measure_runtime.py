#!/usr/bin/env python3
"""
Executes async_comprehension four times in parallel
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel and measures
    the total runtime.

    Returns:
        float: The total runtime of the executions.
    """
    start_time = time.time()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    total_time = time.time() - start_time
    return total_time
