""" Exercise 5a """
#Sterling Clark
#CS 100 2018S Section 02
#HW 00, Jan 21, 2018

""" Exercise 5b """
yearBirth = 1996
topRating = 10
worldPopulation = 7600000000

""" Exercise 5c """
weight = 20.35
pi = 3.14
centimeters = 0.01

""" Exercise 5d """
coolPhrase = "All for one, and one for all"
popularMovie = "Avengers"
direction = "north"

""" Textbook Exercise 1-1 """

'''1'''
#Trying to print without either parenthesis will result in the compiler interpreting the function as a variable.
#If I try to pass it with using only one parenthesis, it skips to the next line, indents, and waits for more input.

'''2'''
#Witout the quotation marks, the compiler thinks you passed a variable as an argument, not a string.
#With a single quotation mark, anything after it becomes part of an incomplete string, and returns an EOL error.

'''3'''
#When putting a plus sign in front of a negative number, the system returns the negative number.
#When doing 2++2, the system returns 4, as if it processed the line like 2+2.

'''4'''
#It is considered an invalid token and returns a sytax error

'''5'''
#Returns a syntax error

""" Textbook Exercise 1-2 """

'''1'''
print(42*60+42)
#Answer: 2562

'''2'''
print(10/1.6)
#Answer: 6.25

'''3'''
print(2562/6.25) #Seconds Per Mile
#Answer: 409.92
print((2562/60)/6.25) #Minutes Per Mile
#Answer: 6.83
print(6.25/((2562/60)/60)) #Miles Per Hour
#Answer: 8.78

""" Textbook Exercise 2-1 """

'''1'''
#This returns an error saying 'Can't assign to literal'

'''2'''
#This returns an error saying 'Can't assign to operator'

'''3'''
#Using a semicolon processes the statement normally

'''4'''
#This returns an error if the statement ends in anything except a whole number.

'''5'''
#The statement 'xy' is not treated as an operation, but as a variable and returns an error because it is undefined.

""" Textbook Exercise 2-2 """

'''1'''
pi=3.141592653589793
print(((4/3)*pi)*(5^3))
#Answer: 25.13

'''2'''
disPrice = 24.95-(24.95*0.4)
print((disPrice * 60)+(.75*59)+3)
#Answer:945.45

'''3'''
time1=3652 #Convert the time to minutes from 0:00
distance1=1
pace1=8.25 #Minutes per Mile
time2=time1+(pace1*distance1)
distance2=3
pace2=7.2
time3=time2+(pace2*distance2)
distance3=1
pace3=8.25
time4=time3+(pace3*distance3)
print(time4)
#Answer: 3690.1 or 7:30am
