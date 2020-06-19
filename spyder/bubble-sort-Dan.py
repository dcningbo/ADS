# -*- coding: utf-8 -*-
"""
Created on Mon May 18 17:43:44 2020

@author: Dan
"""
import random

def bubble(list):
    index_length = len(list) - 1
    sorted = False
    
    while not sorted:
        sorted = True
        for i in range(0, index_length):
            if list[i] > list[i + 1]:
                sorted = False
                list[i], list[i + 1] = list[i + 1], list[i]
                
    return list               
                
list = random.sample(range(1, 7),6)
print(list)
result = bubble(list)
print(result)