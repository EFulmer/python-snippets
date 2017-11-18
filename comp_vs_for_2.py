#!/usr/bin/env python
from string import ascii_lowercase


def dict_for():
    d = {}
    for c in ascii_lowercase:
        if c not in 'aeiou':
            d[c] = ord(c)
    return d


def dict_comp():
    comp = { c: ord(c) for c in ascii_lowercase if c not in 'aeiou' }
    return comp

print('comprehension = {}'.format(dict_comp()))
print('for = {}'.format(dict_for()))
