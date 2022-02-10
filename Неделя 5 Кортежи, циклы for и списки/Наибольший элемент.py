listinput = list(map(int, input().split()))
max_element = listinput[0]
index = 0
for i, e in enumerate(listinput):
    if e > max_element:
        max_element = e
        index = i
print(max_element, index)

# Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке.
# Если наибольших элементов несколько, выведите их значение и индекс первого из них.
# Вводится список чисел. Все числа списка находятся на одной строке.
