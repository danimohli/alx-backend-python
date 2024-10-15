#!/usr/bin/env python3
"""
Measure the total runtime of executing
"""

import asyncio
import random
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Measure the total runtime of executing wait_n(n, max_delay),
    and return the average time taken per coroutine.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay passed to wait_random.

    Returns:
        float: The average time per coroutine.
    """

    elapsed_time: float

    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.perf_counter() - start_time
    return elapsed_time / n
