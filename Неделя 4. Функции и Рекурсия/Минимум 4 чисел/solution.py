def min4(a, b, c, d):
    m1 = min(a, b)
    m2 = min(c, d)
    m_all = min(m1, m2)
    return m_all


m_all, b, c, d = int(input()), int(input()), int(input()), int(input())
print(min(m_all, b, c, d))
