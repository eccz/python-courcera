# это сам, потести append и join, но не совсем по условию
# listinput = list(map(int, input().split()))
# revlist = []
# len_listinput = len(listinput)
# for i in range(len(listinput)):
#     revlist.append(listinput[len_listinput - i - 1])
# print(' '.join(map(str, revlist)))

# Переставьте элементы данного списка в обратном порядке, затем выведите элементы полученного списка.
# Эта задача отличается от предыдущей тем, что вам нужно изменить значения элементов самого списка,
# поменяв местами A[0] c A[n-1], A[1] с A[n-2], а затем вывести элементы списка подряд.
#
# Предлагается в учебных целях проделать это вручную, например, не используя срезов и стандартных функций.
#
# по условию, но спер

a = list(map(int, input().split()))
k = len(a)
i = 0
while i < len(a) // 2:
    a[i], a[k - 1] = a[k - 1], a[i]
    i += 1
    k -= 1
a = list(map(str, a))
print(' '.join(a))
