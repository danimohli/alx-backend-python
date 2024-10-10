#!/usr/bin/env python3
"""
Function annotation with mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sum_mixed_list:
        - mxd_lst as Argument of mixed list of int with float
        - Return: Sum of the list as float
    """
    return sum(mxd_lst)
