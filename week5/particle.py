import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

nn = 50
r = 10
class Particle:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
# a
# cparts = []
# for x in np.linspace(-5, 5, 40):
#     for y in np.linspace(-5, 5, 40):
#         if np.sqrt(x**2 + y**2) <= 5 and np.sqrt(x**2 + y**2) >= 3:
            # cparts.append(Particle(x, y))

# for p in cparts:
#     plt.plot(p.x, p.y, 'mo')
# plt.xlabel('x')
# plt.ylabel('y')
# ax = plt.gca()
# ax.axis('equal')
# plt.show()
#b
cparts = []
for theta in np.linspace(0, 2*np.pi, nn):
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    cparts.append(Particle(x, y))
print(cparts)
for p in cparts:
    plt.plot(p.x, p.y, 'o')
plt.xlabel('x')
plt.ylabel('y')
ax = plt.gca()
ax.axis('equal')
plt.show()

