fin = open('input.txt', 'r', encoding='utf8')
inlist = []
pts9, pts10, pts11 = [], [], []
for line in fin:
    inlist.append(line.split())
for e in inlist:
    if e[2] == '9':
        pts9.append(int(e[3]))
    elif e[2] == '10':
        pts10.append(int(e[3]))
    elif e[2] == '11':
        pts11.append(int(e[3]))

print(max(pts9), max(pts10), max(pts11))
fin.close()
#
# В олимпиаде по информатике принимало участие несколько человек. Победителем олимпиады становится человек,
# набравший больше всех баллов. Победители определяются независимо по каждому классу.
# Определите количество баллов, которое набрал победитель в каждом классе.
# Гарантируется, что в каждом классе был хотя бы один участник.
# Формат ввода:
# Информация о результатах олимпиады записана в файле, каждая строка которого имеет вид:фамилия имя класс балл.
# Фамилия и имя — текстовые строки, не содержащие пробелов.
# Класс - одно из трех чисел 9, 10, 11. Балл - целое число от 0 до 100.
# В этой задаче файл необходимо считывать построчно, не сохраняя содержимое файла в памяти целиком.
# Формат вывода
# Выведите три числа: баллы победителя олимпиады по 9 классу, по 10 классу, по 11 классу.
# Входной файл в кодировке utf-8 (В Python используйте open('input.txt', 'r', encoding='utf-8')).
