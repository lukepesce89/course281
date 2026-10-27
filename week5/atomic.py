import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
anaught = 5.29 * 10**(-11)
x = np.linspace(-20, 20, 100)
y = np.linspace(-20, 20, 100)[:,np.newaxis]
def wave_func(x, y):  
    r = np.sqrt(x**2 + y**2)
    psi = x*(6-r)*np.exp(-r/3)
    return psi
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, wave_func(x, y))
plt.show()

plt.plot(x, wave_func(x, y))
plt.imshow(wave_func(x, y))
plt.colorbar()
plt.show()