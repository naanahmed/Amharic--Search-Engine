import codecs

with codecs.open('Doc1.txt', encoding='utf-8') as f:
    lines = f.read()
    f.close()

print(lines.split('\n', 1)[1][:100])