# -*- coding: utf-8 -*-
"""
Created on Fri May  8 18:50:24 2020

@author: Dan
"""

def dec2bin(dec_num):
    bin_num = []
    q = 0
    r = 0
    while dec_num > 0:
        q = dec_num // 2
        r = dec_num % 2
        bin_num.insert(0, r)
        dec_num = q
    return bin_num

#decimal = input("Enter number to convert: ")
#decimal = int(decimal)
decimal = 129

result = (dec2bin(decimal))
#result = str(result)
#result = result.replace(', ', '')
#''.join(map(*result, sep='')
print("The binary equivalent of {} is:".format(decimal))
print(*result, sep='')