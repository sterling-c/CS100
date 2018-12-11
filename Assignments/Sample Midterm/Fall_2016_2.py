"""
Sterling Clark
Sample Exam 2016F Ver.2
CS100-002
"""

#2
'''
spell = 'accio'
         01234
1)
freq = 0
pointer = 0
letter = a
freq = 1
pointer = 1
2)
freq = 1
pointer = 1
letter = c
freq = 2
pointer = 2
DONE

ANSWER: C
'''

#5
'''
substances = ['oobleck', 'flubber']
vowels = 'aeiou'
1)
'a' in 'oobleck' = false
print 'o'
'e' in 'oobleck' = true
2)
'a' in 'flubber' = false
print f
'e' in 'flubber' = true
DONE

Answer: E
'''

#7
'''
contents = ['You', 'would', 'not', 'think', 'to', 'look', 'at', 'him', 'but', 'he', 'was', 'famous', 'long', 'ago', 'For', 'playing', 'the', 'electric', 'violin', 'on', 'Desolation', 'Row']
1)
word = You
len(word) == 3 = True
count = 1
2)
word = would
len(word) == 3 = False
count = 1
3)
word = not
len(word) == 3 = True
count = 2
4)
word = think
len(word) == 3 = False
count = 2
5)
word = to
len(word) == 3 = False
count = 2
6)
word = look
len(word) == 3 = False
count = 2
7)
word = at
len(word) == 3 = False
count = 2
8)
word = him,
len(word) == 3 = False
count = 2
9)
word = but
len(word) == 3 = True
count = 3
10)
word = he
len(word) == 3 = False
count = 3
11)
word = was
len(word) == 3 = True
count = 4
12)
word = famous
len(word) == 3 = False
count = 4
13)
word = long
len(word) =0= 3 = False
count = 4
14)
word = ago
len(word) == 3 = True
count = 5
15)
word = For
len(word) == 3 = True
count = 6
16)
word = playing
len(word) == 3 = False
count = 6
17)
word = the
len(word) == 3 = True
count = 7
18)
word = electric
len(word) == 3 = False
count = 7
19)
word = violin
len(word) == 3 = False
count = 7
20)
word = on
len(word) == 3 = False
count = 7
21)
word = Desolation
len(word) == 3 = False
count = 7
22)
word = row
len(word) == 3 = True
count = 8

ANSWER: B
'''

#8
'''
d = {'drink':['beer'], 'burger':['veggie', 'beef'], 'salad':'beet'}
x ='ee'
1)
ee in drink = false
ee in burger = false
ee in salad = false
2)
ee in drink.values() = false
ee in burger.values() = false
ee in salad.values() = false
3)
ee in beer = true
ee in veggie = false
ee in beef = true
ee in beet = true
return beer
DONE
ANSWER: C
'''

#10
'''
words = ['I', 'heard', 'the', 'roar', 'of', 'a', 'wave', 'that', 'could', 'drown', 'the', 'whole', 'world']
wordList = ['a','of','the']
1)
word = I
word in wordList = false
word[0] == 'w' = false
rtn = [I]
2)
word = heard
word in wordList = false
word[0] == 'w' = false
rtn = [I, heard]
3)
word = the
word in wordList = true
continue
rtn = [I, heard]
4)
word = roar
word in wordList = false
word[0] == 'w' = false
rtn = [I, heard, roar]
5)
word = of
word in wordList = true
continue
rtn = [I, heard, roar]
6)
word = a
word in wordList = true
continue
rtn = [I, heard, roar]
7)
word = wave
word in wordList = false
word[0] == 'w' = true
break
rtn = [I, heard, roar, wave]
DONE

Answer: D
'''

#12
def wordLengths(text):
    dict = {}
    words = text.split()
    for word in words:
        length = len(word)
        if(length not in dict):
            dict[length] = 1
        else:
            dict[length] += 1
    return dict

#13
def initVowelCount(inFile, outFile):
    in_F = open(inFile, 'r')
    out_F = open(outFile, 'w')
    vowels = 'aeiouAEIOU'
    for line in in_F:
        vowelCount = 0
        words = line.split();
        for word in words:
            for vowel in vowels:
                if(vowel == word[0]):
                    vowelCount += 1
        if(vowelCount == 0):
            out_F.write("\n");
        else:
            out_F.write(str(vowelCount) + "\n");
    in_F.close()
    out_F.close()
