import pandas as pd
import numpy as np
from numpy import cos, sin
import matplotlib.pyplot as plt
from scipy import linalg

def rot(theta):
    R = np.array(((cos(theta), -sin(theta)), (sin(theta), cos(theta))))
    return R
print (rot(90))