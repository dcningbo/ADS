# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 20:44:36 2020

@author: Dan
"""

def Shift(vector, i, j):
    if i <= j:
        return vector
    store = vector[i-1]
    for k in range(0, i-j):
        vector[i-k-1] = vector[i-k-2]
    vector[j] = store
    return vector

vector = [2,3,4,1,5]
# vector = [1,2,3,0,4]
Shift(vector, 5, 3)
Shift(vector, 3, 1)
print(vector)