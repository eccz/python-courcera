mydict = dict()
mylist = []
votes = 0
with open('input.txt', 'r', encoding='utf8') as fin:
    for line in fin:
        mydict[line.strip()] = mydict.get(line.strip(), 0) + 1
        votes += 1

mylist = sorted(mydict, key=lambda x: (-int(mydict[x]), x))

with open('output.txt', 'w', encoding='utf8') as fout:
    if int(mydict[mylist[0]]) * 2 > votes:
        print(mylist[0], file=fout)
    else:
        print(mylist[0], mylist[1], sep='\n', file=fout)
#
# В выборах Президента Российской Федерации побеждает кандидат, набравший свыше половины числа голосов избирателей.
# Если такого кандидата нет, то во второй тур выборов выходят два кандидата, набравших наибольшее число голосов.
#
# Формат ввода
#
# Каждая строка входного файла содержит имя кандидата, за которого отдал голос один избиратель.
# Известно, что общее число кандидатов не превосходит 20,
# но в отличии от предыдущих задач список кандидатов явно не задан.
# Читайте данные из файла input.txt с указанием кодировки utf8.
#
# Формат вывода
#
# Если есть кандидат, набравший более 50% голосов, программа должна вывести его имя.
# Если такого кандидата нет, программа должна вывести имя кандидата, занявшего первое место,
# затем имя кандидата, занявшего второе место. Выводите данные в файл output.txt с указанием кодировки utf8.
# Тест 2
# Входные данные:
# Полуэкт Варфоломеев
# Варфоломей Виссарионов
# Виссарион Полуэктов
# Варфоломей Виссарионов
# Варфоломей Виссарионов
# Полуэкт Варфоломеев
#
# Вывод программы:
# Варфоломей Виссарионов
# Полуэкт Варфоломеев
