import numpy as np
import matplotlib.pyplot as plt

x = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

b = (np.mean(x * y) - np.mean(x) * np.mean(y)) / (np.mean(x ** 2) - np.mean(x) ** 2)
a = np.mean(y) - b * np.mean(x)
print(a, b)
# 444.1773573243596 2.620538882402765

x = x.reshape((10, 1))
y = y.reshape((10, 1))
b1 = np.dot(np.linalg.inv(np.dot(x.T, x)), x.T @ y)
print(b1)
# [[5.88982042]]
plt.scatter(x, y)
plt.plot(x, b1 * x)
plt.plot(x, a + b * x)
plt.show()
