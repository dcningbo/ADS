# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:44:34 2020

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

def binary(v, num):
    n = len(v)
    L = 1
    R = n
    while R >= L:
        m = math.floor((L+R)/2)
        if num >= n:
            break
        elif v[m] == num:
            return m+1
        elif v[m] > num:
            R = m - 1
        else:
            L = m + 1
    return False

num = int(input("Number to searh for: "))
# num = int(num)

v = np.random.randint(1,20,20)
print(v)
sorted = bubble(v, len(v)-1)
print(sorted)
result = binary(sorted, num)
if result == False:
    print("Your number is not in the vector.")
else:
    print("The number {} is in the {}th position of vector v.".format(num, result))
