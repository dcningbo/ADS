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

def sort(v, r):
    if r <= 1:
        return v
    sort(v, r-1)
    j = r
    i = r
    while v[i] < v[j-1] and j > 0:
        j = j-1
    shift(v,i,j)
    return v

def insertion(v):
    n = len(v)-1
    return sort(v,n)

v = np.random.randint(1,50,30)
print(v)
sorted = insertion(v)
print(sorted)
