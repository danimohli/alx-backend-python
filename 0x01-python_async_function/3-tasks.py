#!/usr/bin/env python3
"""
Regular function that takes an integer max_delay
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Regular function that takes an integer max_delay and
    returns an asyncio.Task

    Args:
        max_delay (int): Maximum delay in seconds for wait_random.

    Returns:
        asyncio.Task: A task object that runs the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
