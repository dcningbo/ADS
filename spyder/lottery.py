# -*- coding: utf-8 -*-
"""
Created on Sun May 10 16:38:50 2020

@author: Dan
"""

#def lottery(birthdays):
#    dates = []
#    i = 1
#    while i <= len(birthdays):
#        count = 0
#        j = 1
#        while j <= len(birthdays):
#            if birthdays[i] == birthdays[j]:
#                count += 1
#            j += 1
#        if count == 1:
#            n = len(dates + 1)
#            dates[n] = birthdays[i - 1]
#        i =+ 2
#    return dates
#
#birthdays = [1, 103, 2, 1212, 3, 103, 4, 309]
#winner = lottery(birthdays)
#print(winner)
    



'''
Deigo Cabrejas' solution
'''

n = 0
numbers = []
birthdays = []

def searchBirthday(birthdays, birthday):
    for idx, value in enumerate(birthdays):
        if value == birthday:
            return idx
    return False

while True:
    play = input("Do you want to enter a new birthday (y/n) ? ")
    if play == 'n':
        break
    birthday = input("Birthday (dd-mm): ")
    idx = searchBirthday(birthdays, birthday)
    if idx is not False:
        del birthdays[idx]
        del numbers[idx]
    else:
        birthdays.append(birthday)
        n += 1
        numbers.append(n)
    print('Your number is ' + str(n))
    
print('The winners are: ')
print(numbers)
print(birthdays)









