import matplotlib.pyplot as plt
import numpy as np
from numpy import exp
import pandas as pd
from dfit import Dfit

def gauss(x, aa, x0, w, bb0):
    return (aa*exp(-(x-x0)**2/(2*w**2)) + bb0)

def lorentz(x, aa, x0, w, bb0):
    return ((aa/(1+((x-x0)/w)**2)) + bb0)

gl1 = pd.read_excel('week6/gl1.xlsx')
gl2 = pd.read_excel('week6/gl2 (1).xlsx')

c0, c1 = list(gl1)
xs1 = gl1[c0].to_numpy()
ys1 = gl1[c1].to_numpy()

d0, d1 = list(gl2)
xs2 = gl2[d0].to_numpy()
ys2 = gl2[d1].to_numpy()


print(f'A={max(ys1)-min(ys1)}, x0={xs1[np.argmax(ys1)]}, B={min(ys1)}')
guesses = [1.5, -1.2, 1, -0.2]
gauss_fit = Dfit(gauss, xs1, ys1, p0s=guesses)
gauss_fit.plotfit(xlabel='x (cm)', ylabel='y (mV)')
gauss_fit.printfit()

print(f'A={max(ys2)-min(ys2)}, x0={xs2[np.argmax(ys2)]}, B={min(ys2)}')
guesses2 = [1.6, 0.6, 1, -0.4]
lorentz_fit = Dfit(lorentz, xs2, ys2, p0s=guesses2)
lorentz_fit.plotfit(xlabel='x (cm)', ylabel='y (mV)')
lorentz_fit.printfit()

gauss_fit2 = Dfit(gauss, xs2, ys2, p0s=guesses2)
gauss_fit2.plotfit(xlabel='x (cm)', ylabel='y (mV)')
gauss_fit2.printfit()

lorentz_fit2 = Dfit(lorentz, xs1, ys1, p0s=guesses)
lorentz_fit2.plotfit(xlabel='x (cm)', ylabel='y (mV)')
lorentz_fit2.printfit()

#assigning gl2 to the gaussian function and gl1 to the lorentzian function return much smaller reduced chi-squareds than the other way around, so this is the best fit.