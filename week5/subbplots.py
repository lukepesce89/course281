import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

xs = np.linspace(0, 1, 300)

plt.subplots_adjust(hspace=.5)
plt.subplot(221)
plt.plot(xs, xs**1)
plt.subplot(222)
plt.plot(xs, xs**1)
plt.subplot(223)
plt.plot(xs, xs**1)
plt.subplot(224)
plt.plot(xs, xs**1)
plt.show()