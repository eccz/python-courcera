def phib(z):
    global n, f1, f2, f, y
    if n < y:
        n += 1
        f = f1 + f2
        f1 = f2
        f2 = f
        return phib(n)
    else:
        return f


x = int(input())
y = x
f1 = 0
f2 = 1
f = 1
n = 1
print(phib(x))
