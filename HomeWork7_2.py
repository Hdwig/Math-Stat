import numpy as np

X = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110], dtype=np.float64)
y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832], dtype=np.float64)


def mse_(B1, y=y, X=X, n=10):
    return np.sum((B1 * X - y) ** 2) / n


n = 10
B1 = 0.1
alpha = 0.000001

for i in range(500):
    B1 -= alpha * (2 / n) * np.sum((B1 * X - y) * X)
    if i % 10 == 0:
        print("B1 = {}".format(B1))

for i in range(10000):
    B1 -= alpha * (2 / n) * np.sum((B1 * X - y) * X)
    if i % 100 == 0:
        print("Iteration: {i}, B1 = {B1}, mse = {mse}".format(i=i, B1=B1, mse=mse_(B1)))
