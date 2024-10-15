#!/usr/bin/env python3
"""
10 random numbers asynchronously from async_generator
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers asynchronously from async_generator.

    Returns:
        List[float]: A list of 10 random float numbers
        collected asynchronously.
    """
    return [num async for num in async_generator()]
