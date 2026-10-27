# Luke Pesce
# Physics 281
# HW 1
# 10/08/26


# Problem 1, Catalan Numbers: finding all catalan numbers up to 1 billion by using a while loop and setting an if statement to stop it once c passes 1 billion.
c = 1
n = 0
print('C_0 = 1')
while True:
    c = c*(4*n + 2)//(n+2)
    if c > 1000000000:
        break
    n += 1
    print(f'C_{n} = {c}')

# Problem 2, Curve Plotting:
# 2a Deltoid Curve plotted by iterating theta from 0 to 2pi and then solving for r, x, and y and creating lists of x and y.
import numpy as np
from numpy import pi, cos, sin, linspace, exp, sqrt
import matplotlib.pyplot as plt
xpoints_delt = []
ypoints_delt = []
for theta_delt in linspace(0, 2 * pi, 100):
    x_delt = 2*cos(theta_delt) + cos(2*theta_delt)
    y_delt = 2*sin(theta_delt) - sin(2*theta_delt)
    xpoints_delt.append(x_delt)
    ypoints_delt.append(y_delt)

plt.plot(ypoints_delt, xpoints_delt)
plt.xlabel(r'$y$')
plt.ylabel(r'$x$')
plt.title('Deltoid Curve')
plt.show()
#2b Galilean Curve plotted by iterating theta from 0 to 10pi and then solving for r, x, and y and creating lists of x and y.
xpoints_gal = []
ypoints_gal = []
for theta_gal in linspace(0, 10*pi, 200):
    r_gal = theta_gal**2
    x_gal = r_gal*cos(theta_gal)
    y_gal = r_gal*sin(theta_gal)
    xpoints_gal.append(x_gal)
    ypoints_gal.append(y_gal)
plt.plot(xpoints_gal, ypoints_gal)
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.title(r'Galilean Curve for $0 \leq \theta \leq 10\pi$')
plt.show()
#2c Fey's Function plotted by iterating theta from 0 to 24pi and then solving for r, x, and y, and creating a list of x and y.
xpoints_fey = []
ypoints_fey = []
for theta_fey in linspace(0, 24*pi, 1000):
    r_fey = exp(cos(theta_fey)) - 2*cos(4*theta_fey) + (sin(theta_fey/12))**5
    x_fey = r_fey*cos(theta_fey)
    y_fey = r_fey*sin(theta_fey)
    xpoints_fey.append(x_fey)
    ypoints_fey.append(y_fey)
plt.plot(xpoints_fey, ypoints_fey)
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.title(r"Fey's Function from $0 \leq \theta \leq 24\pi$")
plt.show()
# Problem 3, Plotting STM Data by reading the file using pandas, then inputing it into imshow to create a density plot.
import pandas as pd

df = pd.read_csv('hw1/stm.txt', header=None, sep=r'\s+')
plt.imshow(df)
plt.title('STM Density Plot')
plt.colorbar()
plt.show()

# Problem 4, Quantum harmonic oscillator plotted by creating a list of the 4 n values, then iterating over a range of 4 and creating a plot for each.
# All plots combined using plt.subplot
import scipy 
n_values = [0, 1, 2, 50]
for i in range(4):
    n = n_values[i]
    x_max = 2*sqrt(n+1)
    x = np.linspace(-x_max, x_max, 5000)
    H = scipy.special.eval_hermite(n,x)
    p = exp(-x**2)*(H)**2
    plt.subplot(2, 2, i+1)
    plt.plot(x, p)
    plt.title(f'n = {n}')
plt.subplots_adjust(hspace=.5)
plt.show()