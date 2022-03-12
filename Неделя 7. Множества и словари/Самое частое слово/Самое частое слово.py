mydict = {}
with open('input.txt') as fin:
    for line in fin:
        for word in line.strip().split():
            mydict[word] = mydict.get(word, 0) + 1
answer = sorted(mydict, key=lambda x: (-int(mydict[x]), x))
print(answer[0])

# Дан текст. Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
