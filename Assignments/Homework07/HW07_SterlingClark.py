"""Sterling Clark
   Assignment 7
   CS100-002"""

'''1'''

def twoWords(length, firstLetter):
    firstWord = ""
    secondWord = ""
    while(True):
        fWord = input("Enter a " + str(length) + "-letter word please: ")
        if(len(fWord) == length):
            firstWord = fWord
            break
    while(True):
        sWord = input("Enter a word beginning with " + firstLetter + " please: ")
        if(sWord[0] == firstLetter):
            secondWord = sWord
            break
    return [firstWord, secondWord]

'''2'''

def twoWordsV2(length, firstLetter):
    firstWord = ""
    secondWord = ""
    fBool = False
    sBool = False
    while(fBool == False):
        fWord = input("Enter a " + str(length) + "-letter word please: ")
        if(len(fWord) == length):
            firstWord = fWord
            fBool = True
    while(sBool == False):
        sWord = input("Enter a word beginning with " + firstLetter + " please: ")
        if(sWord[0] == firstLetter):
            secondWord = sWord
            sBool = True
    return [firstWord, secondWord]

'''3'''

def enterNewPassword():
    while(True):
        password = input("Enter a password between 8-15 characters: ")
        if(len(password) > 8 and len(password) < 15 and any(char.isdigit() for char in password)):
            print("Success")
            break
        else:
            print("Fail")

'''4'''
import random
def GuessNumber():
    randNum = random.randint(0, 51)
    guessNum = 1
    while(guessNum <= 5):
        guess = input("Guess " + str(guessNum) + "? ")
        if(int(guess) == randNum):
            print("Correct")
            break
        elif(int(guess) > randNum):
            print("Too high")
        elif(int(guess) < randNum):
            print("Too low")
        if(guessNum == 5):
            print("The correct answer is: " + str(randNum))
        guessNum += 1        
    
