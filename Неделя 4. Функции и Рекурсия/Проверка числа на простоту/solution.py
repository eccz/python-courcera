def isprime(n):
    i = 2
    while i <= n:
        if n % i == 0 and n != 2:
            return 'NO'
        elif i >= n**0.5:
            return 'YES'
        else:
            i += 1


x = int(input())
print(isprime(x))
