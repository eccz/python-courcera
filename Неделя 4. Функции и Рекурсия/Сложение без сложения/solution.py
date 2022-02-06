def sum(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    return sum(a + 1, b - 1)


x, y = int(input()), int(input())
print(sum(x, y))
