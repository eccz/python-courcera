s = str(input())
i = 1
print(s[0], end='')
while i < len(s):
    print('*', end='')
    print(s[i:i + 1:], sep='', end='')
    i += 1
