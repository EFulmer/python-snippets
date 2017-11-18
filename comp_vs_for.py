#!/usr/bin/env python
"""demonstrate how comprehensions are like building iterables through for loops"""
from string import ascii_lowercase


def dict_for() -> dict:
    """return a dictionary mapping lowercase ASCII chars to their code points"""
    d = {}
    for c in ascii_lowercase:
        d[c] = ord(c)
    return d


def dict_comp() -> dict:
    """return a dictionary mapping lowercase ASCII chars to their code points"""
    comp = {c: ord(c) for c in ascii_lowercase}
    return comp

print(f'comprehension = {dict_comp()}')
print(f'for = {dict_for()}')
print(f'comprehension == for? {dict_comp() == dict_for()}')
