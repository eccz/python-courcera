mydict = dict()
text = []
with open('input.txt') as fin:
    # text = fin.read().split() # читает весь файл, решение далее - построчно
    for line in fin:
        for word in line.split():
            text.append(word)

for word in text:
    if word not in mydict:
        mydict[word] = 0
    print(mydict[word], end=' ')
    mydict[word] += 1

# Во входном файле (вы можете читать данные из файла input.txt) записан текст.
# Словом считается последовательность непробельных подряд идущих символов.
# Слова разделены одним или большим числом пробелов или символами конца строки.
# Для каждого слова из этого текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.
