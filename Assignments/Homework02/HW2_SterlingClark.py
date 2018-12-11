"""
Sterling Clark
CS100-002
Homework 2
"""
'''1'''
import turtle
t = turtle.Turtle()
for i in range(3):
    t.fd(100)
    t.lt(120)
for i in range (4):
    t.fd(100)
    t.lt(90)
for i in range(5):
    t.fd(100)
    t.lt(72)
'''2'''
for i in range(5):
    t.circle(50*i)
    t.penup()
    t.right(90)
    t.fd(50)
    t.pendown()
    t.left(90)
'''3'''
import math
print(math.factorial(100))
print(math.log2(1000000))
print(math.gcd(63,49))
