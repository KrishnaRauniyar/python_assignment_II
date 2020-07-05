# Write code that will print out the anagrams (words that use the same
# letters) from a paragraph of text.


class Word(object):
    def __init__(self, string, index):
        self.string = string
        self.index = index
# dupArray contains array of words
def createDupArray(string, size):
    dupArray = []
    # copy words from the given wordArray to dupArray
    for i in range(size):
        dupArray.append(Word(string[i], i))
    return dupArray

def printAnagramsTogether(wordArr, size):
    dupArray = createDupArray(wordArr, size)
    # sorting
    for i in range(size):
        dupArray[i].string = ''.join(sorted(dupArray[i].string))
    dupArray = sorted(dupArray, key=lambda k: k.string)

    for word in dupArray:
        print(wordArr[word.index])


sent = "cat dog tac god low pow wop wol"
a = sent.split()
wordArr = a
size = len(wordArr)
printAnagramsTogether(wordArr, size)


