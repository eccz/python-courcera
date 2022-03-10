states_count = int(input())
city_list = []
mydict = {}
for i in range(states_count):
    temp = input().split()
    for item in temp[1::]:
        mydict[item] = temp[0]

city_count = int(input())
for i in range(city_count):
    city_list.append(input().strip())
for i in city_list:
    print(mydict.get(i, 0))

# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.
#
# Формат ввода
#
# Программа получает на вход количество стран N.
# Далее идет N строк, каждая строка начинается с названия страны, затем идут названия городов этой страны.
# Название каждого город состоит из одного слова.
# В следующей строке записано число M, далее идут M запросов — названия каких-то M городов, перечисленных выше.
#
# Формат вывода
#
# Для каждого из запроса выведите название страны, в котором находится данный город.
# 2
# Russia Moscow Petersburg Novgorod Kaluga
# Ukraine Kiev Donetsk Odessa
# 3
# Odessa
# Moscow
# Novgorod
#
# Вывод программы:
# Ukraine
# Russia
# Russia
