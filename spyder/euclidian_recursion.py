# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:02:14 2020

@author: Dan
"""

def gcd(a,b):
    if a == b:
        return a
    elif a > b:
        return gcd(a-b, b)
    else:
        return gcd(a, b-a)
    

print(gcd(121,88))