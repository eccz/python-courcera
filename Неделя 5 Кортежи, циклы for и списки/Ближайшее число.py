array_size = int(input())
inputlist = list(map(int, input().split()))[:array_size:]
x = int(input())
min1 = inputlist[0]
delta = abs(x - min1)
for i in inputlist:
    if delta > abs(x - i):
        delta = abs(x - i)
        min1 = i
print(min1)

# Напишите программу, которая находит в массиве элемент, самый близкий по величине к  данному числу.
# В первой строке задается одно натуральное число N, не превосходящее 1000 – размер массива.
# Во второй строке содержатся N чисел – элементы массива (целые числа, не превосходящие по модулю 1000).
# В третьей строке вводится одно целое число x, не превосходящее по модулю 1000.
# Вывести значение элемента массива, ближайшее к x. Если таких чисел несколько, выведите любое из них.
