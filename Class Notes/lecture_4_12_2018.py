def wordCount(inFile, outFile):
    in_F = open(inFile, 'r')
    out_F = open(outFile, 'w')
    for line in in_F:
        wordList = line.split()
        wordCount = len(wordList)
        out_F.write(str(wordCount) + '\n')
    in_F.close()
    out_F.close()

