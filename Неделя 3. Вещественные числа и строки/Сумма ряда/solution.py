n = int(input())
i = 1
z = 0
while i <= n:
    z += 1 / i**2
    i += 1
if z == int(z):
    print('{0:.1f}'.format(z))
else:
    print('{0:.5f}'.format(z))

