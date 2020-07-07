# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 19:48:14 2020

@author: Dan
"""
def pibirthday(birthday):
    for i in range(0, len(pi)):
        if pi[i] == birthday[0]:
            count = 0
            for j in range(0, len(birthday)):
                if pi[i+j] == birthday[j]:
                    count += 1
                else:
                    break
                if count == len(birthday):
                    return i


birthday = input("Enter your birthday in 'D/M/YY' format:")  
birthday = list(map(int, birthday))                  
p = open('one_mil_pi.txt')
pi = p.read()
pi = pi.replace(' ', '')
pi = pi.replace('.', '')
pi = list(map(int, pi))

piday = pibirthday(birthday)
print("Your birthday starts on the {} digit of pi.".format(piday))
                

#
    