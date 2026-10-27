import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from dfit import Dfit

data2 = pd.read_excel('week6/data2.xlsx')
# print(list(data2))
c0, c1, c2 = list(data2)
xs = data2[c0].to_numpy()
ys = data2[c1].to_numpy()
yerrs = data2[c2].to_numpy()


def linmod(x,p0,p1):
    return p0 + p1 * x

def polynomialmod(x, p0, p1, p2, p3, p4, p5):
    return p0 + p1 * x + (p2 * (x**2)) + p3*(x**3) + p4*(x**4) + p5*(x**5)
# plt.errorbar(xs, ys, yerrs, fmt='go', capsize=5)
# plt.xlabel(c0)
# plt.ylabel(c1)

linfit = Dfit(polynomialmod, xs, ys, yerrs, varies=[True, True])
linfit.plotfit(xlabel= 'x (cm)', ylabel= 'y (mV)')
linfit.printfit()

quadfit = Dfit(polynomialmod, xs, ys, yerrs, varies=[True, True, True])
quadfit.plotfit(xlabel= 'x (cm)', ylabel= 'y (mv)')
quadfit.printfit()

cubfit = Dfit(polynomialmod, xs, ys, yerrs, varies=[True, True, True, True])
cubfit.plotfit(xlabel= 'x (cm)', ylabel= 'y (mV)')
cubfit.printfit()
# xmods = np.linspace(-1, 8, 300)
# p0 =-1.5
# p1 =0.75
# ymods = linmod(xmods, p0, p1)
# plt.plot(xmods, ymods,'b-')
# plt.show()
