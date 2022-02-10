def IsAscending(A):
    i = 1
    n = len(A)
    while i <= n - 1 and A[i] > A[i - 1]:
        i += 1
    return i == n


list_inp = list(map(int, input().split()))
if IsAscending(list_inp):
    print('YES')
else:
    print('NO')

# Дан список. Определите, является ли он монотонно возрастающим
# (то есть верно ли, что каждый элемент этого списка больше предыдущего).
# Выведите YES, если массив монотонно возрастает и NO в противном случае.
# Решение оформите в виде функции IsAscending(A).
# В данной функции должен быть один цикл while,
# не содержащий вложенных условий и циклов — используйте схему линейного поиска.
