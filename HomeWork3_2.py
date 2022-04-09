from math import factorial


def okrug(p):
    return p * 100000 // 1 / 100000


def com(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


a = com(8, 2)
b = com(12, 4)
answer = (com(5, 2) / a) * (com(5, 1) * com(7, 3) / b) + (com(5, 1) * com(3, 1) / a) * (com(5, 2) * com(7, 2) / b) + (
        com(3, 2) / a) * (com(5, 3) * com(7, 1) / b)
print(okrug(answer))
