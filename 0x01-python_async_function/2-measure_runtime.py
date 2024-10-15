#!/usr/bin/env python3
"""
Measure the total runtime of executing wait_n
"""
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total runtime of executing wait_n(n, max_delay),
    and return the average time taken per coroutine.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay passed to wait_random.

    Returns:
        float: The average time per coroutine.
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    total_time = time.time() - start_time

    return total_time / n
