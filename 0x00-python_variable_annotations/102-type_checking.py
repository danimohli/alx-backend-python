#!/usr/bin/env python3
"""
Type Checking  funct
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    zoom_array:
        - lst Argument as tuple int
        - factor Argument as int, with defaul value 2
        - Return: list of int
    """

    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in
