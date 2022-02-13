n = int(input())
inputlist = list(map(int, input().split()))[:n:]
print(*sorted(inputlist))
