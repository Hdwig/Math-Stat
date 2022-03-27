import numpy as np

t = 2.262
v = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])
X = np.mean(v)
sqo = np.std(v, ddof=1)
n = 10 ** 0.5
dim = X - t * (sqo / n)
dip = X + t * (sqo / n)
# (110.557; 25.643)
