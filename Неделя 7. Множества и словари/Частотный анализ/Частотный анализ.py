mydict = dict()
mylist = []
with open('input.txt') as fin:
    for line in fin:
        for word in line.strip().split():
            mydict[word] = mydict.get(word, 0) + 1
for k, e in mydict.items():
    mylist.append((e, k))

for e in sorted(mylist, key=lambda x: (-int(x[0]), x[1])):
    print(e[1])
#
# Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
# Слова должны быть отсортированы по убыванию их количества появления в тексте,
# а при одинаковой частоте появления — в лексикографическом порядке.
#
# Указание.
#
# После того, как вы создадите словарь всех слов, вам захочется отсортировать его по частоте встречаемости слова.
# Желаемого можно добиться, если создать список, элементами которого будут кортежи из двух элементов:
# частота встречаемости слова и само слово. Например, [(2, 'hi'), (1, 'what'), (3, 'is')].
# Тогда стандартная сортировка будет сортировать список кортежей, при этом кортежи сравниваются по первому элементу,
# а если они равны —то по второму. Это почти то, что требуется в задаче.
# Тест 2
# Входные данные:
# oh you touch my tralala
# mmm my ding ding dong
#
# Вывод программы:
# ding
# my
# dong
# mmm
# oh
# touch
# tralala
# you
