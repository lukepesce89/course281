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
np.savetxt('foo.txt',array,fmt='%d',newline='\r\n')
#6
plt.plot(np.linspace(0, 1, 100),np.linspace(0, 1, 100))
plt.show()