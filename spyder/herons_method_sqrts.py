# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 21:09:23 2020

@author: Dan
"""

def square_root(x,n):
    g = x
    count = 1
    temp_value = ((g * 10**n) + 0.5) - ((x/g)*10**n + 0.5)
    while ((g * 10**n) + 0.5) - ((x/g)*10**n + 0.5) != 0:
        count += 1
        temp_value = ((g * 10**n) + 0.5) - ((x/g)*10**n + 0.5)
        g = 0.5 * (g + (x/g))
        print(count)
    return g


result = square_root(42, 5)

print(result)


