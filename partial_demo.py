# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 17:08:09 2020

@author: 1
"""

int('111111', base = 2)

def int2(x, base=2):
    return int(x, base)

print(int2('1000000'))

import functools
int2 = functools.partial(int, base=2)
print(int2('1000001'))