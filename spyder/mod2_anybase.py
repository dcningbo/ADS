# -*- coding: utf-8 -*-
"""
Created on Fri May 15 21:56:38 2020

@author: Dan
"""

def last_digit(n):
    return n % 10

def mod2(n):
    return last_digit(n) % 2

n = input("Enter number:")
n = int(n)
result = mod2(n)

print('{} in mod 2 is {}'.format(str(n), str(result)))