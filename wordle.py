from os.path import basename

def main():
    basePath = __file__.removesuffix(basename(__file__))

    wordListPath = basePath + "words.txt"

    wordFile = open(wordListPath, mode="r")

    words = []
    for line in wordFile:
        if len(line.removesuffix("\n")) == 5:
            #words.append(line)
            words.append(line.removesuffix("\n"))

    wordFile.close()
    
    '''newWordFile = open(basePath + "newWords.txt", "w")
    for word in words:
        newWordFile.write(word)'''
    
    moreWords = []
    moreWordsFile = open(basePath + "moreWords.txt")
    for line in moreWordsFile:
        if len(line.removesuffix("\n")) == 5:
            moreWords.append(line.removesuffix("\n"))

    for word in words:
        try:
            moreWords.index(word)
        except ValueError:
            print(word)




    

if __name__ == "__main__":
    main()