import numpy as np

d = 25
sqo = d ** 0.5
n = 27
X = 174.2
z = 1.96
dip = X + z * (sqo / 27 ** 0.5)
dim = X - z * (sqo / 27 ** 0.5)
print(dim, dip)
# (176.086 ; 172.313)
