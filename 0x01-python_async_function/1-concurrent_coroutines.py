#!/usr/bin/env python3
"""
Asynchronous routine that spawns `wait_random` n times with a maximum delay
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns `wait_random` n times with
    a maximum delay of max_delay.

    Args:
        n (int): Number of times to spawn `wait_random`.
        max_delay (int): Maximum delay passed to `wait_random`.

    Returns:
        List[float]: List of all delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]

    delays = [await task for task in asyncio.as_completed(tasks)]

    return delays
