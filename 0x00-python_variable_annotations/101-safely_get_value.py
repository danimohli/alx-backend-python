#!/usr/bin/env python3
'''
Type-annotated function to safely retrieve a value from a dictionary.
'''
from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping[Any, T], key: Any,
                     default: Def = None) -> Res:
    '''Retrieves a value from a dictionary using a given key.

    Args:
        dct (Mapping): The dictionary to retrieve the value from.
        key (Any): The key to look for in the dictionary.
        default (Def, optional): The value to return if the key is not found.

    Returns:
        Res: The value associated with the key if found, otherwise default
    '''
    if key in dct:
        return dct[key]
    else:
        return default
