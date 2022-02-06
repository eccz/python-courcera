n = int(input())
f0, f1, i = 1, 0, 0
while i < n:
    f = f0 + f1
    f0 = f1
    f1 = f
    i += 1
print(f1)
