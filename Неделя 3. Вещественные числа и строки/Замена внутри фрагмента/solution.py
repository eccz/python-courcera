s = str(input())
first = s.find('h') + 1
last = s.rfind('h')
print(s[:first:], s[first:last:].replace('h', 'H'), s[last::], sep='')
