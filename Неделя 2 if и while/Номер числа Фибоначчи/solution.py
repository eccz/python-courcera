n = int(input())
f0, f1, i = 1, 0, 0
while f1 < n:
    f = f0 + f1
    f0 = f1
    f1 = f
    i += 1
if f1 != n:
    print(-1)
else:
    print(i)
