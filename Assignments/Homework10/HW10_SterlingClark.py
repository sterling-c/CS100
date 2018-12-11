#Sterling Clark5
#Homework 10
#CS100-002

#1
def file_copy(in_file, out_file):
    in_f = open(in_file, 'r')
    out_f = open(out_file, 'w')
    for line in in_f:
        out_f.write(line + '\n')
#2
def file_stats(in_file):
    in_f = open(in_file, 'r')
    characters = 0
    words = 0
    lines = 0
    text = ''
    while True:
        char = in_f.read(1)
        characters += 1
        text += char
        if(char == ''):
            break
    wordList = text.split()
    words += len(wordList)
    lines = len(text.split('\n'))
    print("Lines: " + str(lines) + "\n")
    print("Words: " + str(words) + "\n")
    print("Characters: " + str(characters) + "\n")
#3
def repeat_words(in_file, out_file):
    in_f = open(in_file, 'r')
    out_f = open(out_file, 'w')
    
    for line in in_f:
        dupeWords = {}
        lineText = line.split()
        for word in lineText:
            lowerWord = word.lower()
            properWord = ''.join(e for e in lowerWord if e.isalnum())
            if(properWord not in dupeWords):
                dupeWords[properWord] = 1
            else:
                dupeWords[properWord] += 1
        for dupeWord in dupeWords:
            if(dupeWords[dupeWord] > 1):
                out_f.write(dupeWord + " ")
        out_f.write("\n")
            
