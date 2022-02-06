a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
o = a * d - b * c
if o != 0:
    o1 = e * d - f * b
    o2 = a * f - e * c
    print(o1 / o, o2 / o)
