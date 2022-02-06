s = str(input())
fs = s.find('f', 0)
if fs != -1:
    print(s.find('f', fs + 1))
else:
    print(-2)
