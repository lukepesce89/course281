import numpy as np
from numpy import cos, sin

def trap(f, a, b, nn):
    h = (b-a)/nn
    wts = np.ones(nn+1)
    wts[0]=0.5
    wts[-1]=0.5
    xs = np.linspace(a, b, nn+1)
    print(wts)

def igrnd(x):
    return sin(x)


b = 3.0
print(f'exact: {1-cos(b)}')
for nn in (5, 10, 20):
    print(f'trap result with {nn} slices = {trap(igrnd,0,b,nn)}')