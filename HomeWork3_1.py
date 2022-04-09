import numpy as np


def okrug(p):
    return p * 100 // 1 / 100


z = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])
z.sort()
print(z)

n = len(z)
f = 0
for i in range(0, n - 1):
    f += z[i]

sa = f / n
sko = 0
for i in range(0, n):
    sko += (z[i] - sa) ** 2
o = ((sko / n) ** 0.5)
o = okrug(o)
print(f"Среднее арефмитическое равно - {sa}")
print(f"Среднее квадратичное отклонение - {o}")
print(f"Дисперсия - {okrug(sko / n)}")
print(f"Несмещенная оценка дисперсии - {(okrug(sko / (n - 1)))}")
