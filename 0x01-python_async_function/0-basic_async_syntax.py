#!/usr/bin/env python3
"""
Asynchronous coroutine that waits for a random delay
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between
    0 and max_delay seconds.

    Args:
        max_delay (int): Maximum number of seconds to delay. Default is 10.

    Returns:
        float: The actual delay time in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
