# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 14:38:24 2020

@author: Dan
"""
import numpy as np

def bubble(v, size):
    if size <= 1:
        return v
    for i in range(0, len(v)-1):
        if v[i] > v[i+1]:
            temp = v[i]
            v[i] = v[i+1]
            v[i+1] = temp
    return bubble(v, size - 1)


v = np.random.randint(1,50,20)
bubble(v, len(v))    
print(v)
        