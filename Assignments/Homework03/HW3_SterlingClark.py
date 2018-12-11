"""
Sterling Clark
CS100-002
Homework 3
"""

'''1'''
print('Excercise 1')
a=3
b=4
c=5
if(a<b):
    print('ok')
if(c<b):
    print('ok')
if(a+b==c):
    print('ok')
if((a^2)+(b^2)==(c^2)):
    print('ok')

'''2'''
print('Excercise 2')
a=3
b=4
c=5
if(a<b):
    print('OK')
else:
    print('NOT OK')
if(c<b):
    print('OK')
else:
    print('NOT OK')
if(a+b==c):
    print('OK')
else:
    print('NOT OK')
if((a^2)+(b^2)==(c^2)):
    print('OK')
else:
    print('NOT OK')

'''3'''
print('Excercise 3')
import turtle
t = turtle.Turtle()
color = input('Give me a color: ')
lWidth = input('Give me a width: ')
lLength = input('Give me a length: ')
shape = input('Give me a shape: ')
t.color(color)
t.width(lWidth)
if(shape=='triangle'):
    for i in range(3):
        t.fd(int(lLength))
        t.lt(120)
if(shape=='square'):
    for i in range(4):
        t.fd(int(lLength))
        t.lt(90)
if(shape=='pentagon'):
    for i in range(5):
        t.fd(int(lLength))
        t.lt(72)

