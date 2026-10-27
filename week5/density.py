import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
x= np.linspace(-20, 20, 100)
y= np.linspace(-20, 20, 100)[:,np.newaxis]
theta = np.arctan2(y, x)
r = np.sqrt(x**2 + y**2)
s = np.cos(r + theta)
print(s)
plt.plot(x, s)
plt.imshow(s)
plt.colorbar()
plt.show()


x2= np.linspace(-20, 20, 100)
y2= np.linspace(-20, 20, 100)[:,np.newaxis]
theta2 = np.arctan2(y2, x2)
r2 = np.sqrt(x**2 + y**2)
w = np.cos(r2 + (theta2/2))
plt.plot(x2, w)
plt.imshow(w)   
plt.colorbar()
plt.show()