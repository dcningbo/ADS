# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 10:08:14 2020

@author: Dan
"""

def gcd(a,b):
    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a
    return a

print(gcd(121,55))