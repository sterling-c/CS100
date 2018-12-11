"""
Sterling Clark
CS100-002
Fall 2015 Sample Midterm
"""

"""Multiple Choice"""
#1: D
#2: A
#3: C
#4: E
#5: C
#6: A
#7: E
#8: C
#9: B
#10: D

"""Programming"""
#11a:
def drawTick(t, tickLen):
    t.pendown()
    t.left(90)
    t.forward(tickLen)
    t.left(180)
    t.forward(tickLen)
    t.left(90)

#11b:
def drawTicks(t, tickLen, numTicks, distance):
    for i in range(numTicks):
        drawTick(t, tickLen)
        t.penup()
        t.forward(distance)

#12:
def beginsWith(letter, strList):
    match = 0
    for word in strList:
        if(word[0]==letter):
            match+=1
    return match

#13:
def greetings(greetStr):
    name = input("What's your name? ")
    day = input("What day is today? ")
    print(greetStr + " " + day + " " + name)
    if(len(name) == len(day)):
        print("Your name has the same number of characters as today!")
    if(len(name) > len(day)):
        print("Your name has more characters than today!")
    if(len(name) < len(day)):
        print("Your name has less characters than today!")
