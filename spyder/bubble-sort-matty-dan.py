# -*- coding: utf-8 -*-
"""
Created on Mon May 18 17:51:34 2020

@author: Dan
"""
import random

def swap(arr, i, j):
    x = arr[j]
    arr[j] = arr[i]
    arr[i] = x
    return arr, i, j
    
    
    
def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        count = 0
        for j in range(0, len(arr) - 1):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count = count + 1
        if count == 0:
            break
    return arr

arr = random.sample(range(0, 10),10)
print(arr)
result = bubble_sort(arr)
print(result)