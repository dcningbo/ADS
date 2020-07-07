# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 13:23:02 2020

@author: Dan
"""

def d2b(n):
    binary_stack = []
    while n/2 != 0:
        binary_stack.insert(0, n%2)
        n = n//2
    return binary_stack


n = input("Enter a number in decimal: ")
n = int(n)
result = d2b(n)
print("{} in binary is:".format(n))
print(*result, sep = "")