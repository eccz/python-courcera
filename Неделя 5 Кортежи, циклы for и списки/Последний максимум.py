inputlist = list(map(int, input().split()))
max_element = 0
max_index = 0
for i, e in enumerate(inputlist):
    if e >= max_element:
        max_element = e
        max_index = i
    print(max_element, max_index)

# Найдите наибольшее значение в списке и индекс последнего элемента,
# который имеет данное значение за один проход по списку,
# не модифицируя этот список и не используя дополнительного списка.
#
# Выведите два значения.
