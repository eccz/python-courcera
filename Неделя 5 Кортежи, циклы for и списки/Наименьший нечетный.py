listinput = list(map(int, input().split()))
print(min([e for e in listinput if e % 2 != 0]))
