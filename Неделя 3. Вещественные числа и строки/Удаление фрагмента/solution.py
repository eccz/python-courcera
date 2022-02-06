s = str(input())
first = (s.find('h', 0))
second = len(s) - s[::-1].find('h') - 1
print(s[0:first], s[second + 1::], sep = '')
#if first == second:
#   print(first)
#elif first != second and first != -1:
#    print(first, second)
