# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 19:06:08 2020

@author: Dan
"""

import math

def binary_recursion(v, num):
    L = 0
    R = len(v)    
    M = math.floor((L+R)/2)
    stack = []
    if L > R:
        return False
    elif v[M] == num:
        return True
    elif v[M] > num:
        for i in range(0, M):
            stack.append(v[i])
        binary_recursion(stack, num)
    elif v[M] < num:
        for i in range(M, len(v)):
            stack.append(v[i])
        binary_recursion(stack, num)
    else:
        return False
    
num = 4
v = [1,2,3,5,10,11]

result = binary_recursion(v, num)
if result == False:
    print("Your number is not in the list")
else:
    print("Your number is in the list")