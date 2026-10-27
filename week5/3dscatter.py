import numpy as np
from numpy import pi, cos, sin, linspace
import matplotlib.pyplot as plt
import pandas as pd

r = 1
nn = 20
xlist = []
ylist = []
zlist = []
for theta in linspace(0, pi, nn):
    for phi in linspace(0, 2*pi, nn):
        xlist.append(r * sin(theta) * cos(phi))
        ylist.append(r * sin(theta) * sin(phi))
        zlist.append(r * cos(theta))

#print(xlist)
#print(ylist)
#print(zlist)

ax = plt.axes(projection = '3d')
ax.scatter(xlist, ylist, zlist)
plt.show()
