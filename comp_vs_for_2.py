#!/usr/bin/env python
"""demostrate how comprehensions using if are like building iterables through for loops and conditionals"""
from string import ascii_lowercase


def dict_for():
    """return a dictionary mapping lowercase ASCII consonants to their code points"""
    d = {}
    for c in ascii_lowercase:
        if c not in 'aeiou':
            d[c] = ord(c)
    return d


def dict_comp():
    """return a dictionary mapping lowercase ASCII chars to their code points"""
    comp = { c: ord(c) for c in ascii_lowercase if c not in 'aeiou' }
    return comp


print(f'comprehension = {dict_comp()}')
print(f'for = {dict_for()}')
