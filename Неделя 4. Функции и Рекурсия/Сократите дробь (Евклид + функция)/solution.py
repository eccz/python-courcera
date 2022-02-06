def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def reducefraction(a, b):
    return a // gcd(a, b), b // gcd(a, b)


x, y = int(input()), int(input())
print(*reducefraction(x, y))
