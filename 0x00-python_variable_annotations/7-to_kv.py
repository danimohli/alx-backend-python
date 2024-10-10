#!/usr/bin/env python3
"""
Type-annotated function to_kv
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    to_kv:
        - k: a string
        - v: an integer or a float
        - Returns: a tuple (k, square of v as float)
    """
    return (k, float(v ** 2))
