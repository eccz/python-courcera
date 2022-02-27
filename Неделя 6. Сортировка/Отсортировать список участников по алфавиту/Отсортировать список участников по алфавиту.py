class Student:
    surname = ''
    name = ''
    score = 0


def surnamesort(std):
    return std.surname


fin = open('input.txt', 'r', encoding='utf8')
inlist, outlist = [], []
for line in fin:
    inlist.append(line.split())
for e in inlist:
    std = Student()
    std.surname = e[0]
    std.name = e[1]
    std.score = int(e[3])
    outlist.append(std)
outlist.sort(key=surnamesort)
for std in outlist:
    print(std.surname, std.name, std.score)
# [print(std.surname, std.name, std.score) for std in outlist]
fin.close()

# Известно, что фамилии всех участников — различны. Сохраните в массивах список всех участников и выведите его,
# отсортировав по фамилии в лексикографическом порядке. При выводе указываете фамилию, имя участника и его балл.
# Используйте для ввода и вывода файлы input.txt и output.txt с указанием кодировки utf8.
# Например, для чтения откройте файл с помощью open('input.txt', 'r', encoding='utf8').
# Входные данные:
# Строки вида "Фамилия Имя НомерШколы Балл".
# Выходные данные
# Строки вида "Фамилия Имя Балл", отсортированные по фамилии.
