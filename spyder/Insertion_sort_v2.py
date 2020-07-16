# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 16:26:29 2020

@author: Dan
"""
import numpy as np

def insertionSort(v):
   for i in range(1,len(v)):

     currentvalue = v[i]
     position = i

     while position > 0 and v[position-1] > currentvalue:
         v[position] = v[position-1]
         position = position-1

     v[position] = currentvalue


v = np.random.randint(1,50,20)
print(v)
insertionSort(v)
print(v)