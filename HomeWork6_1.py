import numpy as np

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

a = []
p = 0
for i in range(0, 10):
    p = (zp[i] * ks[i])
    a.append(p)
#    a = [14035, 25830, 166060, 183800, 18360, 51730, 35262, 135300, 89520, 91520]
p0 = 0
for i in range(0, 10):
    p0 += a[i]
p0 = p0 / 10
p1 = 0
for i in range(0, 10):
    p1 += zp[i]
p2 = 0
for i in range(0, 10):
    p2 += ks[i]
xy = (p1 / 10) * (p2 / 10)
cov = p0 - xy
cov2 = np.mean(zp * ks) - np.mean(zp) * np.mean(ks)
cov3 = np.cov(zp, ks, ddof=0)
# cov = 9157.839 = cov2 = cov3
sqox = np.std(zp, ddof=0)
# 174.55
sqoy = np.std(ks, ddof=0)
# 59.115
Rxy = cov/(sqoy*sqox)
# 0.8874
rxy = np.corrcoef(zp, ks)
# 0.8874





