"""
Sterling Clark
Homework k5
CS100-002
"""

'''1a'''
def hasFinalLetter(strList,letters):
    newList = []
    for i in range(len(strList)):
        if(strList[i][-1] == letters):
            newList.append(strList[i])
    print(newList)

'''1b'''
list1 = ["run", "home", "String", "DEA", "create", "hussle"]
list2 = ["Mask", "drink", "HEART", "hunter", "fail", "SUCCESS"]
list3 = ["valley", "harp", "fight", "crash", "wet", "sun"]

hasFinalLetter(list1, "e")
hasFinalLetter(list1, "q")
hasFinalLetter(list2, "S")
hasFinalLetter(list2, "I")
hasFinalLetter(list3, "t")
hasFinalLetter(list3 , "l")

'''2a'''
def isDivisible(maxInt, twoInts):
    divisors = []
    for i in range(1, maxInt):
        if(i%twoInts[0] == 0 and i%twoInts[1] == 0):
            divisors.append(i)
    print(divisors)

'''2b'''
tuple1 = (3,2)
tuple2 = (3,4)
tuple3 = (6,15)
isDivisible(30, tuple1)
isDivisible(72, tuple1)
isDivisible(60, tuple2)    
isDivisible(5, tuple2)
isDivisible(80, tuple3)
isDivisible(1000, tuple3)
