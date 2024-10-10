#!/usr/bin/env python3
"""
Type annotations for safely_get_value function
"""
from typing import Mapping, Any, TypeVar, Union

# Define a TypeVar for the type of the default value
T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any, default:
                     Union[T, None] = None) -> Union[T, None]:
    """
    safely_get_value:
        - dct: A mapping (like a dictionary) containing key-value pairs
        - key: The key to search for in the mapping
        - default: The value to return if the key is not found
        - Returns: The value associated with d key / default if key is nt found
    """
    if key in dct:
        return dct[key]
    else:
        return default
