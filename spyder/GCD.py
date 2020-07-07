# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 10:16:13 2020

@author: Dan
"""

#def naiveGCD(a,b):
#    best = 0
#    for d in range(0, a+b):
#        if 
        
        

#import sys
#input = sys.stdin.read()
#tokens = input.split()
#a = int(tokens[0])
#b = int(tokens[1])
#print(a + b)


def naiveGCD(a, b):

    gcd = 0
    for d in range(1, a+b):
       if a % d == 0 and b % d == 0:
            gcd = d
    print(gcd)

naiveGCD(42,48)

'''
More effectient
'''

def effGCD(a, b):
    if b == 0:
        return a
    else:
        return effGCD(b, a%b)
gcd = effGCD(42, 48)
print(gcd)
#
#'''
#Using library
#'''
#import math as m
#
#def efflib(a, b):
#    return m.gcd(a, b)

def effGCD(a, b):
    while b != 0:
        gcd = b
        b = a % b
        a = gcd
    return gcd
gcd = effGCD(42, 48)
print(gcd)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


