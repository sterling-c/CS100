"""
Sterling Clark
Sample Exam 2016S Ver.2
CS100-002
"""

#2
'''
catty = 'cat in the hat'


ANSWER: D
'''

#6
'''


ANSWER: E
'''

#7
'''


ANSWER: C
'''

#8
'''


ANSWER: D
'''
#10
'''


ANSWER:E
'''


#12
def initialDict(text):
    words = text.split()
    initDict = {}
    for word in words:
        key = word[0].lower()
        if(key not in initDict):
            initDict[key] = []
            initDict[key].append(word)
        else:
            initDict[key].append(word)
    return initDict

#13
def lineStats(infile, outfile):
    in_F = open(infile, 'r')
    out_F = open(outfile, 'w')
    for line in in_F:
        content = line.replace('\n', '')
        wordList = content.split()
        wordCount = len(wordList)
        charCount = 0
        for word in wordList:
            charCount += len(word)
        out_F.write(str(wordCount) + ' ' + str(charCount) + '\n')
    in_F.close()
    out_F.close()

