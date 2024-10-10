#!/usr/bin/env python3
"""
Annotate element_length function with appropriate types
"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    element_length:
        - lst: Iterable containing sequences
        - Returns: List of tuples, where each tuple has a sequence
                   and its length
    """
    return [(i, len(i)) for i in lst]
