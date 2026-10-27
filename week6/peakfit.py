import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from dfit import Dfit

data_peak = pd.read_excel('week6/peak4.xlsx')
# print(list(data_peak))
c0, c1 = list(data_peak)
xs = data_peak[c0].to_numpy()
ys = data_peak[c1].to_numpy()

from numpy import exp
def gauss(x, aa, x0, w, bb0, bb1):
    return (aa*exp(-(x-x0)**2/(2*w**2)) + bb0 + bb1*x)


guesses = [3, 5, 1, 1, 0]
peak_fit = Dfit(gauss, xs, ys, p0s=guesses)
peak_fit.plotfit(xlabel='x (cm)', ylabel='y (mV)')
peak_fit.printfit()



from numpy import exp
def gauss2(x, aa, x0, w, bb0, bb1, bb2):
    return (aa*exp(-(x-x0)**2/(2*w**2)) + bb0 + bb1*x + bb2*(x**2))

guesses2 = [3, 5, 1, 1, 0]
peak_fit2 = Dfit(gauss2, xs, ys, p0s=guesses2)
peak_fit2.plotfit(xlabel='x (cm)', ylabel='y (mV)')
peak_fit2.printfit()