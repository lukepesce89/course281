import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class RightTriangle:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
    def hyp(self):
        return np.sqrt(self.l1**2 + self.l2**2)
    def angle1(self):
        return np.degrees(np.arccos(self.l1/self.hyp()))
    def angle2(self):
        return np.degrees(np.arccos(self.l2/self.hyp()))

t = RightTriangle(1, np.sqrt(3))
print(t.hyp())
print(t.angle1())
print(t.angle2())