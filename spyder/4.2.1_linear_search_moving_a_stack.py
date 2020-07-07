# -*- coding: utf-8 -*-
"""
Created on Fri May  8 13:12:33 2020

@author: Dan
"""

stack = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot']
queue = []

for i in range(0, len(stack)):
    t = stack.pop(0)
    queue.append(t)
    
print(queue)    
    
    
    
    