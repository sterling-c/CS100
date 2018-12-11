"""
Sterling Clark
CS100-002
Sample Exam 2017F
"""

#1
'''
s = 'bib'
1)
char = 'b'
d = {}
char not in d == true
result: d('b') = 1
2)
char = 'i'
d = {'b':1}
char not in d == true
result: d('i') = 1
3)
char = 'b'
d = {'b':1,'i':1}
char not in d == false
result: d('b') = 2

ANSWER: C
'''

#5
'''
mixedKeys = {1:{'three':3, 0:'zeroval'}, 0:'zero', 'two':2}
                         [0]               [1]         [2]
[1] refers to the key '1' not the index.
1:{'three':3, 0:'zeroval'}
       [0]        [1]
[0] in this case refers to the key '0'
ANSWER: C
'''

#8
'''
fats = "You broke my heart when you said we'll part"
wordList = ["You", "broke", "my", "heart", "when", "you", "said", "we'll", "part"]
1)
word = "You"
d = {}
initial == "Y"
initial[0] not in d = True
Result: d["Y"] = "You"
2)
word = "broke"
d = {"Y": ["You"]}
initial == "b"
initial[0] not in d = True
Result: d["b"] = "broke"
3)
word = "my"
d = {"Y": ["You"], "b": ["broke]}
initial == "m"
initial[0] not in d = True
Result: d["m"] = "my"
4)
word = "heart"
d = {"Y": ["You"], "b": ["broke], "m": ["my"]}
initial == "h"
initial[0] not in d = True
Result: d["h"] = "Heart"
5)
word = "when"
d = {"Y": ["You"], "b": ["broke], "m": ["my"], "h": ["heart]}
initial == "w"
initial[0] not in d = True
Result: d["w"] = "when"
6)
word = "you"
d = {"Y": ["You"], "b": ["broke], "m": ["my"], "h": ["heart], "w": ["when"]}
initial == "y"
initial[0] not in d = True
Result: d["y"] = "you"
7)
word = "said"
d = {"Y": ["You"], "b": ["broke], "m": ["my"], "h": ["heart], "w": ["when"], "y": ["you"]}
initial == "s"
initial[0] not in d = True
Result: d["s"] = "said"
8)
word = "we'll"
d = {"Y": ["You"], "b": ["broke], "m": ["my"], "h": ["heart], "w": ["when"], "y": ["you"], "s": ["said"]}
initial == "w"
initial[0] not in d = False
Result: d["w"].append("we'll")
9)
word = "part"
d = {"Y": ["You"], "b": ["broke], "m": ["my"], "h": ["heart], "w": ["when", "we'll"], "y": ["you"], "s": ["said"]}
initial == "p"
initial[0] not in d = True
Result: d["p"] = "part"

Answer: B
'''


#9
'''
num = 3
content = "The affair is so simple and yet baffles us altogether"
words = ["The", "affair", "is", "so", "simple", "and", "yet", "baffles", "us", "altogether"]
1)
word = "The"
(len(word) != 3) = False
different = 0
2)
word = "affair"
(len(word) != 3) = True
different = 1
3)
word = "is"
(len(word) != 3) = True
different = 2
4)
word = "so"
(len(word) != 3) = True
different = 3
5)
word = "simple"
(len(word) != 3) = True
different = 4
6)
word = "and"
(len(word) != 3) = False
different = 4
7)
word = "yet"
(len(word) != 3) = False
different = 4
8)
word = "baffles"
(len(word) != 3) = True
different = 5
9)
word = "us"
(len(word) != 3) = True
different = 6
10)
word = "altogether"
(len(word) != 3) = False
different = 7

ANSWER: E
'''

#10
'''
fred = 'power concedes nothing without a demand'
1)
freq = {}
thing = power
freq[power] = 1
2)
freq = {'power':1}
thing = concedes
freq[concedes] = 1
3)
freq = {'power':1, 'concedes':1}
thing = nothing
freq[nothing] = 1
4)
freq = {'power':1, 'concedes':1, 'nothing':1}
thing = without
freq[without] = 1
5)
freq = {'power':1, 'concedes':1, 'nothing':1, 'without':1}
thing = a
freq[a] = 1
6)
freq = {'power':1, 'concedes':1, 'nothing':1, 'without':1, 'a':1}
thing = demand
freq[demand] = 1

ANSWER: A
'''
fred = 'power concedes nothing without a demand'
freq = {}
for thing in fred.split():
    freq[thing] = fred.count(thing)
print(len(freq))

#12
def countVowels(text):
    vowels = ['a','e','i','o','u']
    wordDict = {}
    wordList = text.split()
    for word in wordList:
        vCount = 0
        for letter in word:
            if letter in vowels:
                vCount += 1
        wordDict[word] = vCount
    return wordDict
#13
def longestOnLine(inFile, outFile):
    in_F = open(inFile, 'r')
    out_F = open(outFile, 'w')
    for line in in_F:
        longestLength = 0
        wordList = line.split()
        for word in wordList:
            if(len(word) > longestLength):
                longestLength = len(word)
            out_F.write(str(longestLength))
    in_F.close()
    out_F.close()
    
