import numpy as np
from numpy import cos, sin
import matplotlib.pyplot as plt
from scipy import linalg

mm = np.array(((2, 1, 4, 1), (3, 4, -1, 1), (1, -4, 1, 5), (2, -2, 1, 3)))
print(mm)
r = np.array((-4, 3, 9, 7))
print(r)

w, x, y, z = linalg.inv(mm)@r
print(w, x, y, z)

w, x, y, z = linalg.solve(mm, r)
print(w, x, y, z)

dd = np.array(((2, -1), (-1, 2)))
evecs, evals = linalg.eigh(dd)
print(evecs[0], evals[0])
print(evecs[1], evals[1])