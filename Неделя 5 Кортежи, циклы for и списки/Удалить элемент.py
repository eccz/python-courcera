# Сдал:
listinput = list(map(int, input().split()))
index = int(input())
listinput.pop(index)
print(*listinput)

# Дан список из чисел и индекс элемента в списке k.
# Удалите из списка элемент с индексом k, сдвинув влево все элементы, стоящие правее элемента с индексом k.
# Программа получает на вход список, затем число k.
# Программа сдвигает все элементы,а после этого удаляет последний элемент списка при помощи метода pop().
# Программа должна осуществлять сдвиг непосредственно в списке, а не делать это при выводе элементов.
# Также нельзя использовать дополнительный список.

# по заданию:
# for i in range(index, len(listinput) - 1):
#     listinput[i] = listinput[i + 1]
#     print(listinput)
# listinput.pop()
# print(*listinput)
