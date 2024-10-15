#!/usr/bin/env python3
"""
Asynchronous routine that spawns `wait_random` n times with a maximum delay
"""
import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


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
    delays = []

    for _ in range(n):
        delay = await wait_random(max_delay)

        # Inserting delays in ascending order manually without using sort()
        if not delays:
            delays.append(delay)
        else:
            for i in range(len(delays)):
                if delay < delays[i]:
                    delays.insert(i, delay)
                    break
            else:
                delays.append(delay)

    return delays
