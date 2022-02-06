a, b, c, = int(input()), int(input()), int(input())
cosbc = ((b**2 + c**2 - a**2) / (2 * b * c))
cosac = ((a**2 + c**2 - b**2) / (2 * a * c))
cosab = ((a**2 + b**2 - c**2) / (2 * a * b))
print(cosac)
print(cosab)
print(cosbc)
if (a + b) <= c or b + c <= a or c + a <= b:
    print('impossible')
elif cosac == 0 or cosab == 0 or cosbc == 0:
    print('rectangular')
elif cosac > 0 and cosab > 0 and cosbc > 0:
    print('acute')
else:
    print('obtuse')
