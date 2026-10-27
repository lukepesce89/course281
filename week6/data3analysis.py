import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from dfit import Dfit

data3 = pd.read_excel('week6/data3.xlsx')
# print(list(data3))
c0, c1 = list(data3)
xs = data3[c0].to_numpy()
ys = data3[c1].to_numpy()

def polynomialmod(x, p0, p1, p2, p3, p4, p5):
    return p0 + p1 * x + (p2 * (x**2)) + p3*(x**3) + p4*(x**4) + p5*(x**5)


linfit = Dfit(polynomialmod, xs, ys, varies=[True, True])
linfit.plotfit(xlabel= 'x (cm)', ylabel= 'y (mV)')
linfit.printfit()

quadfit = Dfit(polynomialmod, xs, ys, varies=[True, True, True])
quadfit.plotfit(xlabel= 'x (cm)', ylabel= 'y (mv)')
quadfit.printfit()

cubfit = Dfit(polynomialmod, xs, ys, varies=[True, True, True, True])
cubfit.plotfit(xlabel= 'x (cm)', ylabel= 'y (mV)')
cubfit.printfit()


