def height(name, d):
    return 0 if name not in d else height(d[name], d) + 1
# рекурсию скатал

mydict = dict()
for i in range(int(input()) - 1):
    child, parent = input().split()
    mydict[child] = parent
namesfull = set(mydict.keys()) | (set(mydict.values()))
[print(i, height(i, mydict)) for i in sorted(namesfull)]

# В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель.
# Каждом элементу дерева сопоставляется целое неотрицательное число, называемое высотой.
# У родоначальника высота равна 0, у любого другого элемента высота на 1 больше, чем у его родителя.
# Вам дано генеалогическое древо, определите высоту всех его элементов.
#
# Формат ввода
#
# Программа получает на вход число элементов в генеалогическом древе N.
# Далее следует N-1 строка, задающие родителя для каждого элемента древа, кроме родоначальника.
# Каждая строка имеет вид имя_потомка имя_родителя.
#
# Формат вывода
#
# Программа должна вывести список всех элементов древа в лексикографическом порядке.
# После вывода имени каждого элемента необходимо вывести его высоту.
#
# Примечания
#
# Эта задача имеет решение сложности O(n), но вам достаточнонаписать решение сложности O(n²)
# (не считая сложности обращенияк элементам словаря).Пример ниже соответствует приведенному древу рода Романовых.
#
# Тест 1
# Входные данные:
# 9
# Alexei Peter_I
# Anna Peter_I
# Elizabeth Peter_I
# Peter_II Alexei
# Peter_III Anna
# Paul_I Peter_III
# Alexander_I Paul_I
# Nicholaus_I Paul_I
#
# Вывод программы:
# Alexander_I 4
# Alexei 1
# Anna 1
# Elizabeth 1
# Nicholaus_I 4
# Paul_I 3
# Peter_I 0
# Peter_II 2
# Peter_III 2
