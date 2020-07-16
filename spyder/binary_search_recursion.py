# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 19:06:08 2020

@author: Dan
"""

import numpy as np
import math

def bubble(v, size):
    if size <= 1:
        return v
    for i in range(0, len(v)-1):
        if v[i] > v[i+1]:
            temp = v[i]
            v[i] = v[i+1]
            v[i+1] = temp
    return bubble(v, size - 1)

def binary_recursion(v, num, R, L):
    M = math.floor((L+R)/2)
    if L > R:
        return False
    elif v[M] == num:
        return M+1
    elif v[M] > num:
        return binary_recursion(v, num, R-1, L)
    elif v[M] < num:
        return binary_recursion(v, num, R, L+1)
    else:
        return False
    
num = int(input("Number to searh for: "))
v = np.random.randint(0,100,20)

print(v)
sorted_v = bubble(v, len(v)-1)
print(sorted_v)
result = binary_recursion(sorted_v, num, len(sorted_v)-1, 1)
if result == False:
    print("\nThe number {} is not in the vector.".format(num))
else:
    print("\nThe number {} is in the {}th position of vector v.".format(num, result))