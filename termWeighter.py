import math
import codecs
import os, glob


def computeTF(word, doc):
    tfDict = 0
    for w in doc.split():
        if w == word:
            tfDict += 1
    return tfDict

def computeIDF(w, docList):
    import math
    idfDict = 0
    N = len(docList)

    for doc in docList:
        if w in doc:
            idfDict += 1
    if idfDict == 0:
        idf = 0
    else:
        idf = math.log2(N / float(idfDict))

    return idf

def computeCosineSimilarity(arr, qarr, docList, wordList):
    length = []

    cosineArr = []
    l = 0
    ql = 0

    r = len(docList)
    cA = [[0] * 2 for i in range(r)]
    for i in range(int(len(qarr))):
        ql += qarr[i][1] * qarr[i][1]

    for j in range(len(docList)):
        l = 0
        for i in range(len(wordList)):
            if (j < len(docList)):
                l += arr[i][j + 1] * arr[i][j + 1]

        length.append(l)

    innerProduct = []
    for j in range(len(docList)):
        ip = 0
        for i in range(len(wordList)):
            if (j < len(docList)):
                ip += qarr[i][1] * arr[i][j + 1]
        innerProduct.append(ip)
    p = 0
    for i in range(len(innerProduct)):
        p = math.sqrt(ql * length[i])
        if p == 0:
            c = 0
        else:
            c = innerProduct[i] / p
        cosineArr.append(c)

    with codecs.open("SearchResults.txt", "a", encoding='utf-8') as f:
        f.truncate(0)
        f.close()

    with codecs.open("SearchResults.txt", "a", encoding='utf-8') as f:
        for c in cosineArr:
            f.write(str(c))
            f.write('\n')
            f.close
    for i in range(len(docList)):
        cA[i][0] = "Doc" + str(i + 1)
        cA[i][1] = cosineArr[i]

    return cA


def readDocCorpus():
    docList = []
    fname = []
    length = 0
    for filename in glob.glob('IndexList_Doc*.txt'):
        length += 1

    for l in range(length):
        with codecs.open("IndexList_Doc" + str(l + 1) + ".txt", encoding='utf-8') as f:
            lines = f.read()
            docList.append(lines)
    return docList


def readQuery():
    with codecs.open('IndexList_Query.txt', encoding='utf-8') as f:
        lines = f.read()
        f.close()
    return lines


def readIndex():
    index_List = []
    with codecs.open('IndexTerms.txt', encoding='utf-8') as f:
        lines = f.read()
        index_List.append(lines)
    return index_List


def queryWeight():
    query = readQuery()
    index_List = readIndex()
    docList = readDocCorpus()
    s = ''.join(index_List)
    r = len(s.split())
    qarr = [[0] * 2 for d in range(r)]
    i = 0
    for word in s.split():
        qarr[i][0] = word
        qarr[i][1] = computeTF(word, query) * computeIDF(word, docList)
        i += 1

    return qarr


def termWeight():
    docList = readDocCorpus()
    index_List = readIndex()

    # at first we will create an array of c columns and r rows
    s = ''.join(index_List)
    c = len(docList) + 1
    r = len(s.splitlines())

    arr = [[0] * c for i in range(r)]
    i = 0
    for word in s.split():
        j = 0
        arr[i][j] = word
        for doc in docList:
            arr[i][j + 1] = computeTF(word, doc) * computeIDF(word, docList)
            j += 1
        i += 1
    # for r in arr:
    # with codecs.open('tf.txt','a',encoding='utf-8') as f:
    # f.write(' '.join([str(x) for x in r] ))
    # f.write('\n')
    # f.close()
    return arr


def main():
    docList = readDocCorpus()
    index_List = readIndex()

    # at first we will create an array of c columns and r rows
    s = ''.join(index_List)
    c = len(docList) + 1
    r = len(s.splitlines())

    cA = computeCosineSimilarity(termWeight(), queryWeight(), docList, s.split())
    cS = sorted(cA, key=lambda l: l[1], reverse=True)
    for r in cS:
        print(' '.join([str(x) for x in r]))
    # print(len(cS))

    return cS


main()
