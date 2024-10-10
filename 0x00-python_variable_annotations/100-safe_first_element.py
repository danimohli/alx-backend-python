#!/usr/bin/env python3
"""
Duck-typed annotations for safe_first_element
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    safe_first_element:
        - lst: A sequence containing elements of any type
        - Returns: The first element of lst or None if lst is empty
    """
    if lst:
        return lst[0]
    else:
        return None
