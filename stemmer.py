import glob
import codecs
from latinToGeez import convertBack
from geezToLatin import convert
import latinToGeez

encoding = 'utf-8'

# LIST OF SUFFIXES AND PREFIXES
suffix = ['iAäLäŜ', 'aWiW', 'aČäWaL', 'äČaT', 'äČaČHu', 'äČaČäW', 'aLäHu', 'aĞäT', 'aWoČ', 'aLäH', 'aLäŜ', 'aLäČHu',
          'aLaLäČ', 'BaČäWS', 'BaČäW',
          'aČäWN', 'aLäČ', 'aLäN', 'aLaČHu', 'aČHuN', 'aČHu', 'aČHuT', 'WoČNNa', 'WoČN', 'aČäW', 'WoČuN', 'BWoT',
          'aČNM', 'aSäWi', 'BäTä',
          'WoČu', 'äWNa', 'oČuN', 'äÑaNäTM', 'äÑaNa', 'äÑaNäT', 'äÑaN', 'äÑaWM', 'äÑaW', 'ÑaWa', 'BäTN', 'aČHuM',
          'aČäW', 'oWa', 'äČW',
          'äČu', 'iču', 'NäW', 'NäT', 'aLu', 'aČN', 'aČW', 'KuM', 'KuT', 'KäW', 'äČN', 'äČM', 'äČH', 'äČŜ', 'äČN',
          'äČW', 'YuŜN', 'YuŜ', 'äWi',
          'oČNNa', 'aWi', 'BäČ', 'oČ', 'oČu', 'WoN', 'äÑa', 'ÑaWN', 'ÑaW', 'oČN', 'äÑ', 'äM', 'ŜW', 'KM', 'äW', 'TM',
          'Wo', 'WM', 'WN', 'NM', 'ŜN',
          'oČ', 'uT', 'iT', 'Ku', 'Wa', 'H', 'Ŝ', 'u', 'K', 'ä', 'äČ', 'uN', 'N', 'M', 'No', 'W', 'i']

prefix = ['SLäMaY', 'YäMaT', 'LaYa', 'ANDä', 'YäTä', 'BäMa', 'eNDä', 'AäL', 'SLä', 'MäS', 'AYä', 'AäS', 'AäT', 'AäY',
          'YaL',
          'SaT', 'SaN', 'SaY', 'SaL', 'YaS', 'Yä', 'Bä', 'Lä', 'Kä', 'AN', 'AL', 'Y', 'T', 'ä']

#TEST WORDS

wordList = []
docList = []
length = 0
for filename in glob.glob('IndexList_Doc*.txt'):
    length += 1

for l in range(length):
    with codecs.open("IndexList_Doc" + str(l + 1) + ".txt", encoding='utf-8') as f:
        lines = f.read()
        docList.append(lines)


# STEMMER FUNCTION - NORMALIZE AND REMOVES PREFIXES AND SUFFIXES FROM THE TEST WORD
def stemmer(s):
    finalstr = s
    if 'AeNDa' in s:
        finalstr = s.replace("AeNDa", "Ao")
    if 'ĊaL' in s:
        finalstr = s.replace("ĊaL", "ṬaL")
    if ('eäS' in s) and ('Ñ' == s[len(s) - 1]):
        finalstr = s.replace("eäS", "S")
    if ('äLa' in s) and len(s) > 2:
        finalstr = s.replace('äLa', 'ä')
        finalstr = finalstr.strip(finalstr[0:2])

    if len(finalstr) > 3:
        for s in suffix:
            if finalstr.endswith(s):
                finalstr = finalstr[:-len(s)]

        for p in prefix:
            if finalstr.startswith(p):
                finalstr = finalstr[len(p):]
    return finalstr


def containsVowel(s):
    if ('ä' in s) or ('u' in s) or ('i' in s) or ('a' in s) or ('e' in s) or ('o' in s):
        return True
    else:
        return False


def clearIndex():
    i = 1
    for doc in docList:
        with codecs.open("IndexList_Doc" + str(i) + ".txt", "a", encoding='utf-8') as f:
            f.truncate(0)
            f.close()
        i += 1


def stemDocuments():
    clearIndex()
    j = 1
    for doc in docList:
        for x in doc.split('\n'):

            # CONVERT WORD TO CV FORM
            st = convert(x)

            # CONVERT WORD BACK TO ROOT/STEM FORM BY CHECKING IF A PAIR OF WORDS CONTAIN VOWELS
            string = ''
            i = 0
            while i <= len(stemmer(st)) - 1:
                if containsVowel(stemmer(st)[i:i + 2]):
                    if not containsVowel(stemmer(st)[i]):
                        string += convertBack(stemmer(st)[i:i + 2])
                        i = i + 2
                    else:
                        string += convertBack(stemmer(st)[i])
                        i = i + 1
                else:
                    string += convertBack(stemmer(st)[i])
                    i = i + 1
            with codecs.open("IndexList_Doc" + str(j) + ".txt", "a", encoding='utf-8') as f:
                if len(string) >= 1:
                    f.write(string)
                    f.write('\n')
        f.close()
        j += 1


def readQuery():
    with codecs.open("IndexList_Query.txt", encoding='utf-8') as f:
        query = f.read();
        f.close()
    return query


def clearQuery():
    with codecs.open("IndexList_Query.txt", 'a', encoding='utf-8') as f:
        f.truncate(0)
        f.close()


def stemQuery():
    query = readQuery()
    query = ' '.join(query.split())
    clearQuery()
    for word in query.split():
        st = convert(word)
        # CONVERT WORD BACK TO ROOT/STEM FORM BY CHECKING IF A PAIR OF WORDS CONTAIN VOWELS
        string = ''
        i = 0
        while i <= len(stemmer(st)) - 1:
            if containsVowel(stemmer(st)[i:i + 2]):
                if not containsVowel(stemmer(st)[i]):
                    string += latinToGeez.convertBack(stemmer(st)[i:i + 2])
                    i = i + 2
                else:
                    string += latinToGeez.convertBack(stemmer(st)[i])
                    i = i + 1
            else:
                string += latinToGeez.convertBack(stemmer(st)[i])
                i = i + 1
        with codecs.open("IndexList_Query.txt", "a", encoding='utf-8') as f:
            f.write(string)
            f.write('\n')
            f.close()


def createIndexList():
    i = 1
    indexList = []
    iList = []
    for doc in docList:
        with codecs.open('IndexList_Doc' + str(i) + '.txt', encoding='utf-8') as f:
            lines = f.read()
            iList.append(lines)
            f.close()
        i += 1

    for doc in iList:
        with codecs.open('IndexTerms.txt', 'a', encoding='utf-8') as f:
            f.truncate(0)
            f.close()

    for doc in iList:
        for word in doc.split():
            if word not in indexList:
                indexList.append(word)
                with codecs.open('IndexTerms.txt', 'a', encoding='utf-8') as f:
                    f.write(word)
                    f.write('\n')

        f.close()


stemDocuments()