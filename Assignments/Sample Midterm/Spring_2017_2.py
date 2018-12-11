#Sterling Clark
#Sample Midterm 2017 Spring
#CS100-002

def inFileCount(fileName):
    inF = open(fileName)
    length = len(inF.read())
    inF.close()
    return length
outF = open('cat.txt', 'w')
outF.write('The sun did not shine.' + '\n')
outF.write('It was too wet to play.' + '\n')
outF.close()
print(inFileCount('cat.txt'))



"""
1)A
2)B
3)C
4)A
5)D
6)E
7)D
8)B
9)C
10)E
"""
