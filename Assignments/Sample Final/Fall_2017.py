"""
Sterling Clark
Spring 2017 Final
CS100-002
"""

#12
def lineStats(inFile, outFile):
    in_F = open(inFile, 'r')
    out_F = open(outFile, 'w')
    for line in in_F:
        wordList = line.split()
        numWords = len(wordList)
        goodLine = line.replace('\n', '')
        numChar = 0
        for char in goodLine:
            numChar += 1
        out_F.write("words " + str(numWords) + " chars " + str(numChar))
    in_F.close()
    out_F.close()

#13
def vowelEndings(text):
    endDict = {}
    vowels = 'aeiou'
    wordList = text.split()
    for word in wordList:
        if(word[-1] in vowels):
            if (word[-1] not in endDict):
                endDict[word[-1]] = []
            endDict[word[-1]].append(word)
    return endDict
