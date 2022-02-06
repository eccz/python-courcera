n = int(input())
i = n
minD = n
while i > 1:
    if n % i == 0:
        minD = i
    i = i - 1
print(minD)
