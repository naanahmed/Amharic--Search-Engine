import os, glob
import codecs

docList = []
fname = []
length = 0
for filename in glob.glob('Doc*.txt'):
    length += 1

for l in range(length):
    with codecs.open("Doc" + str(l + 1) + ".txt", encoding='utf-8') as f:
        lines = f.read()
        docList.append(lines)


def tokenizeDocuments():
    i = 1
    for doc in docList:
        with codecs.open("IndexList_Doc" + str(i) + ".txt", "a", encoding='utf-8') as f:
            f.truncate(0)
            f.close()
        i += 1

    j = 1
    for doc in docList:
        for word in doc.split():
            word = word.replace('።', '')
            word = word.replace('፡፡', '')
            word = word.replace('÷', '')
            word = word.replace('፥', '')
            word = word.replace('፣', '')
            word = word.replace('“', '')
            word = word.replace('”', '')

            with codecs.open("IndexList_Doc" + str(j) + ".txt", "a", encoding='utf-8') as f:
                f.write(word)
                f.write("\n")
                f.close()
        j += 1


def clearQuery():
    with codecs.open("IndexList_Query.txt", "r+", encoding='utf-8') as f:
        f.truncate(0)
        f.close()


def tokenizeQuery():
    clearQuery()
    i = 1
    with codecs.open("query.txt", encoding='utf-8') as f:
        lines = f.read()
        new_string = lines[0:]
        for word in new_string.split():
            word = word.replace('።', '')
            word = word.replace('፡፡', '')
            word = word.replace('÷', '')
            word = word.replace('፥', '')
            word = word.replace('፣', '')
            word = word.replace('“', '')
            word = word.replace('”', '')

            with codecs.open("IndexList_Query.txt", "a", encoding='utf-8') as f:
                f.write(word)
                f.write("\n")
                f.close()


tokenizeDocuments()