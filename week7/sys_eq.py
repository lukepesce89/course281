import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import linalg

# x + 4*y + z = -4
# 4*x - y - z = 3
# 2*x + y + 3 * z = 7

M = np.array(((1, 4, 1), (4, -1, -1), (2, 1, 3)))
M_inv = linalg.inv(M)
b = np.array((-4, 3, 7))
print(M)
print(b)
method_a = M_inv@b
print(method_a)
method_b = linalg.solve(M, b)
print(method_b)
ans = method_a[0] + 4*method_a[1] + method_a[2]
print(ans)