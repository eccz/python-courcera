inputlist = list(map(int, input().split()))
if len(inputlist) == 3:
    print(*inputlist)
else:
    max1 = max(inputlist)
    min1 = min(inputlist)
    inputlist.remove(max1)
    inputlist.remove(min1)
    max2 = max(inputlist)
    min2 = min(inputlist)
    inputlist.remove(max2)
    max3 = max(inputlist)
    if max1 * max2 * max3 > min1 * min2 * max1:
        print(max1, max2, max3)
    else:
        print(min1, min2, max1)

# В данном списке из n≤10⁵ целых чисел найдите три числа,произведение которых максимально.
# Решение должно иметь сложность O(n), где n - размер списка. То есть сортировку использовать нельзя.
# Выведите три искомых числа в любом порядке.
