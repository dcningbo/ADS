# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 16:26:29 2020

@author: Dan
"""

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position > 0 and alist[position-1] > currentvalue:
         alist[position] = alist[position-1]
         position = position-1

     alist[position] = currentvalue

#alist = [54,26,93,17,77,31,44,55,20]
alist = [5,2,4,6,1,3]
insertionSort(alist)
print(alist)