"""
Sterling Clark
Homework 4
CS100-002
"""

'''1'''
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
for i in range(len(months)):
    if(months[i][0] == 'J'):
        print(months[i])
'''2'''
for i in range(100):
    if(i%2 == 0 and i%5 == 0):
        print(i)
'''3'''
horton = "A person's a person, no matter how small."
vowels =  "aeiouAEIOU"
for i in range(len(horton)):
    for a in range(len(vowels)):
        if(horton[i] == vowels[a]):
            print(horton[i])
