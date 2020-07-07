# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:06:51 2020

@author: Dan
"""

def party(guest_list, max_guests, t):
    for i in range(0, len(guest_list)):
        if t < 6:
            if guest_list[i] == 0:
                max_guests +=1
                t += 1
            elif guest_list[i] == 1:
                max_guests += 1
                t += 2
            else:
                continue
    return max_guests
            
guest_list = [0,2,1,0,1,1]
max_guests = 0
total_people = 0  
          
total_guests = party(guest_list, max_guests, total_people)
print(total_guests)

'''
Zac Bolton
''' 
#import math as math
#
#def bday2(Sweets, Toys, Siblings, N):
#    if len(Siblings) != N:
#        return "invalid input"
#    guests = 0
#    total = 0
#    while total <= N:
#        if (N - total) > min(Siblings):
#            total = total + min(Siblings)
#            guests = guests + 1    
#        Siblings.remove(min(Siblings))
#    if total == N:
#        return guests
#    else:
#        return "no solution"

#Siblings = [1,3,2,1,2,2]
#answer = bday2(42, 48, Siblings, 6)
#print(answer)

'''
instructors algorithm
'''

#m0 = 2
#m1 = 3
#m2 = 1
##i, j, k = 0, 0, 0
##t = i + j + k
#t = 0
#
#for i in range(0, m0+1):
#    for j in range(0, m1+1):
#        for k in range(0, m2+1):
#            if i + (2*j) + (3*k) == 6:
#                if i + j + k > t:
#                    t = i + j + k
#print(t)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    