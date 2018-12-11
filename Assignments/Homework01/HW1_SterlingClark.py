"""
Sterling Clark
Homework 01
1/25/2018
"""

"""2"""
grades=['D','A','C','C','B','F','A','F','C','D']
count=0 #represents the occurence of a letter grade

frequency=[] 
for A in range(len(grades)): #Loops through the entire list
    if 'A' == grades[A]: #Checks if the string matches the current element in the list
        count += 1 
frequency.append(count) #adds the value of count to the list 'frequency'
count=0 #Resets count for the next loop
for B in range(len(grades)):
    if 'B' == grades[B]:
        count += 1
frequency.append(count)
count=0
for C in range(len(grades)):
    if 'C' == grades[C]:
        count += 1
frequency.append(count)
count=0
for D in range(len(grades)):
    if 'D' == grades[D]:
        count += 1
frequency.append(count)
count=0
for F in range(len(grades)):
    if 'F' == grades[F]:
        count += 1
frequency.append(count)
count=0

print(grades)
print(frequency)

"""3"""
dog_breeds = ['collie','sheepdog','Chow','Chihuahua'] #A
herding_breeds = dog_breeds[0:2] #B
print(herding_breeds)
tiny_dogs = dog_breeds[3] #C
print(tiny_dogs)
print('Persian' in dog_breeds) #D

