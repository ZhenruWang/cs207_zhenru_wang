#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 19:27:08 2019

@author: zhenrumacpro
"""

from collections import Counter

def dna_complement (seq):
    seq = seq.upper()
    component = Counter(seq).keys()
    allowed = set('ATGC')
    if (set(component).issubset(allowed) ):
        res = ''
        for c in seq:
            if(c == 'A'):
                res += 'T'
            elif (c == 'T'):
                res += 'A'
            elif (c == 'C'):
                res += 'G'
            elif (c == 'G'):
                res += 'C'
        return res
    else:
        return None

print(dna_complement('AAGcTTc'))