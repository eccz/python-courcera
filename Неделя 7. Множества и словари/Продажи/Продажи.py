# mydict = {}
# with open('testinput.txt') as in_file:
#     for line in in_file:
#         name, item, amount = line.split()
#         mydict[name] = mydict.get(name, dict())
#         mydict[name][item] = mydict[name].get(item, 0) + int(amount)
# for name in sorted(mydict):
#     print(name, ':', sep='')
#     [print(item, mydict[name][item]) for item in sorted(mydict[name])]
#
#
# выше вариант покрасивее
surname_dict = dict()
with open('input.txt') as fin:
    for line in fin:
        temp = line.split()
        man, item, price = temp[0], temp[1], int(temp[2])
        if man not in surname_dict:
            surname_dict[temp[0]] = {item: price}
        elif item not in surname_dict[man]:
            surname_dict[man][item] = price
        else:
            surname_dict[temp[0]][item] += price
for i in sorted(surname_dict):
    print(i, ':', sep='')
    for j in sorted(surname_dict[i]):
        print(j, surname_dict[i][j])
#
# Дана база данных о продажах некоторого интернет-магазина. Каждая строка входного файла представляет собой запись вида
#
# Покупатель товар количество, где
# Покупатель — имя покупателя (строка без пробелов),
# товар — название товара (строка без пробелов),
# количество — количество приобретенных единиц товара.
# Создайте список всех покупателей,
# а для каждого покупателя подсчитайте количество приобретенных им единиц каждого вида товаров.

# Формат ввода
#
# Вводятся сведения о покупках в указанном формате.
#
# Формат вывода
#
# Выведите список всех покупателей в лексикографическом порядке,после имени каждого покупателя выведите двоеточие,
# затем выведите список названий всех приобретенных данным покупателем товаров в лексикографическом порядке,
# после названия каждого товара выведите количество единиц товара, приобретенных данным покупателем.
# Информация о каждом товаре выводится в отдельной строке.
#
# Тест 1
# Входные данные:
# Ivanov paper 10
# Petrov pens 5
# Ivanov marker 3
# Ivanov paper 7
# Petrov envelope 20
# Ivanov envelope 5
#
# Вывод программы:
# Ivanov:
# envelope 5
# marker 3
# paper 17
# Petrov:
# envelope 20
# pens 5
