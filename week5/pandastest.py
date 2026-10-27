import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('week5/gl2_missing.xlsx')
xs = df['x'].to_numpy()
ys = df['y'].to_numpy()
plt.plot(xs, ys, 'bo')
plt.show()