import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import linalg

u = np.array((2, 0))
v = np.array((1, 1))

#u * v = 2*1 + 0*1 = 2 <--- dot product
#<2, 1><0, 1>cos(2)

dotp = u@v
print(f'dot product: {dotp}')

A = np.array(((1, 3), (2, 4), (5, 6)))
B = np.array(((2, 1, 4), (3, 2, 1)))
print(f'A:{A}')
print(f'B:{B}')
print(f'A@B : {A@B}')
print(f'B@A : {B@A}')

#1*2, 


C = np.array(((1, 3, 2), (2, 4, 1), (5, 6, 5)))
C_inv = linalg.inv(C)
print(f'C: {C}')
print(f'inverse: {C_inv}')
print(f'dot product: {C_inv@C}')