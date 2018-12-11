# Sterling Clark
#  CS100-002
#  Homework
"""1"""
def initialLetterCount(wordList):
    firstDict={}
    for word in wordList:
            if(bool(firstDict) == False):
                firstDict[word] = 1
            else:
                for init in firstDict:
                    if(word[0] == init[0]):
                        firstDict[init] += 1
                    else:
                        firstDict[word] = 1
    return firstDict
