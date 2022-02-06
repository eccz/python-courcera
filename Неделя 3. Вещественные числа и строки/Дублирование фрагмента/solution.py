s = str(input())
first = (s.find('h', 0))
second = len(s) - s[::-1].find('h') - 1
print(s[0:first], s[first:second], s[first + 1:second], s[second::], sep='')
