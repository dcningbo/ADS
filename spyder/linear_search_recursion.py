# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:04:42 2020

@author: Dan
"""

def linear(v, i, num):
    if i >= len(v):
        return False
    elif num == v[i]:
        return i
    else:
        return linear(v, i+1, num)
        
        
v = [1,2,3,4,5,6,7,8,9]
num = 5
result = linear(v, 0, num)
print("{} is at index {} of v.".format(num, result +1))