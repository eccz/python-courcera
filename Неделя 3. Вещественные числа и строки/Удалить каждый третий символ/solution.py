s = str(input())
i = 0
while i < len(s):
    if i % 3 == 0:
        i += 1
    else:
        print(s[i], end="")
        i += 1
