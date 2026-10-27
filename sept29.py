import numpy as np
import matplotlib.pyplot as plt
#3
rows = int(input("rows? "))
cols = int(input("cols? "))
array = np.zeros((rows, cols), int)

for r in range(rows):
    for c in range(cols):
        array[r, c] = r * cols + c + 1

print(f'Array:\n {array}')

#4
array_slice_row = array[1:2]
array_slice_col = array[:, 1:2]
array_slice_cube_left = array[0:3, 0:3]
array_slice_cube_right = array[0:3, -3:]
array_transpose = array.T
print(f'Row: {array_slice_row}')
print(f'Column: {array_slice_col}')
print(f'Cube upper left: {array_slice_cube_left}')
print(f'Cube upper right: {array_slice_cube_right}')
print(f'Transposed: {array_transpose}')
#5
np.savetxt('foo.csv',array,fmt='%d',newline='\r\n', delimiter=',', header='values')
#6
n = 0.1
x = np.linspace(0, 201, 1000)
#print(x)
f1 = np.sin(n*x)
f2 = np.cos(n*x)
plt.plot(x, f1, label=r'$\sin(x)$')
plt.plot(x, f2, label=r'$\cos(x)$')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.ylim(.5, -.5)
plt.grid(True)
plt.show()
#7
n2 = 0.1
x2 = np.linspace(0, 201, 20)
print(x2)
f3 = np.sin(n*x2)
f4 = np.cos(n*x2)
plt.plot(x2, f3, label=r'$\tan(x) \cdot cos(x)$', marker='s')
plt.plot(x2, f4, label=r'$\cos(x)$', marker='*', linestyle='none')
plt.xlabel(r'$x$', fontsize=15)
plt.ylabel(r'$\Delta$', fontsize=15)
plt.title(r'$\sin(x)$ vs $\cos(x)$', fontsize=20)
plt.legend()
plt.grid(True)
plt.show()