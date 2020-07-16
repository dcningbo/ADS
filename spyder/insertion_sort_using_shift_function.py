# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 19:27:59 2020

@author: Dan
"""

import numpy as np

def shift(v,i,j):
    if i <= j:
        return v
    store = v[i]
    for k in range(0, i-j-1):
        v[i-k] = v[i-k-1]
    v[j] = store
    return v

def insertion(v):
    for i in range(1, len(v)):
        j = i
        while v[i] < v[j-1] and j > 1:
            j = j-1
        shift(v,i,j)
    return v

v = np.random.randint(1,50,5)
print(v)
sorted = insertion(v)
print(sorted)
