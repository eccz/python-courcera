s = str(input())
first = (s.find('f', 0))
second = len(s) - s[::-1].find('f') - 1
if first == second:
    print(first)
elif first != second and first != -1:
    print(first, second)
