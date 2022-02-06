def MinDivisor(n):
    i = 2
    while i <= n:
        if n % i == 0:
            return i
        elif i >= n**0.5:
            return n
        else:
            i += 1


n = int(input())
print(MinDivisor(n))
