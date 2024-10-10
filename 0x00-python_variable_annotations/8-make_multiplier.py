#!/usr/bin/env python3
"""
Type-annotated function make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier:
        - multiplier: a float
        - Returns: a function that takes a float and returns a float
    """
    def multiplier_function(n: float) -> float:
        return n * multiplier

    return multiplier_function
