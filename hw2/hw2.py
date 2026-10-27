# Luke Pesce
# Physics 281
# HW 2
# 10/15/26

#Problem 1, Gezerlis 1.1 
def fact(n):
     return 1 if n==0 else n*fact(n-1)
print(fact(10))

#My iterative version
def fact_iter(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print(fact_iter(10))
#Both together showing each factorial from 1 to 20
for n in range(20):
    rec = fact(n)
    itr = fact_iter(n)
    print(f'recursive: {rec} iterative: {itr}')

#Problem 2, Gezerlis 1.3, reversing a list
#Unpythonic
xs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def unpythonic():
    for i in range(len(xs)-1, -1, -1):
        print(i, xs[i])
#Pythonic
def pythonic():
    for i, x in reversed(list(enumerate(xs))):
        print(i, x)
unpythonic()
print()
pythonic()

#Problem 3 Mandelbrot Set
import numpy as np
import matplotlib.pyplot as plt
N = 50 #intializing N as 50
n_max = 10 #setting the limit to 10
#making an array of 0's
image = np.zeros((N, N)) 
for row in range(N):
    for col in range(N):
        #assigning X, Y for each point
        X = -2 + 3 *col / (N-1)
        Y = -1.5 + 3 * row /(N-1)
        x, y = X, Y
        for n in range(1, n_max+1):
            #applying the equation to the array
            if (x**2+y**2) > 4:
                image[row, col] = n
                break
            x, y = x**2 - y**2 + X, 2*x*y + Y
print(image)
#generating the plot
plt.imshow(image, extent=(-2, 1, -1.5, 1.5), origin='lower')
plt.colorbar()
plt.show()