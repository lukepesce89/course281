import matplotlib.pyplot as plt
import numpy as np
from numpy import exp
import pandas as pd
from dfit import Dfit

def decay(t, tau, N_0):
    return (N_0*exp(-t/tau)+25)

dec1 = pd.read_excel('week7/decay1.xlsx')
dec2 = pd.read_excel('week7/decay2.xlsx')

c0, c1 = list(dec1)
xs1 = dec1[c0].to_numpy()
ys1 = dec1[c1].to_numpy() 

b0, b1 = list(dec2)
xs2 = dec2[b0].to_numpy()
ys2 = dec2[b1].to_numpy()     



sig1 = np.sqrt(ys1)
sig2 = np.sqrt(ys2)

# plt.figure()
# plt.errorbar(xs1, ys1, sig1, fmt='bo')
# plt.xlabel('Time (min)')
# plt.ylabel('Counts/min')
# plt.title('Decay 1')
# plt.show()

# plt.figure()
# plt.errorbar(xs2, ys2, sig2, fmt='bo')
# plt.xlabel('Time (min)')
# plt.ylabel('Counts/min')
# plt.title('Decay 2')
# plt.show()

plt.figure()
plt.errorbar(xs1, ys1, sig1, fmt='bo')
plt.yscale('log')
plt.xlabel('Time (min)')
plt.ylabel('Counts/min')
plt.title('Decay 1')
plt.show()

plt.figure()
plt.errorbar(xs2, ys2, sig2, fmt='bo')
plt.yscale('log')
plt.xlabel('Time (min)')
plt.ylabel('Counts/min')
plt.title('Decay 2')
plt.show()

guesses = [3, 5]
decay1fit = Dfit(decay, xs1, ys1, p0s=guesses)
decay1fit.plotfit()
decay1fit.printfit()

guesses2 = [3, 5]
decay2fit = Dfit(decay, xs2, ys2, p0s=guesses2)
decay2fit.plotfit()
decay2fit.printfit()