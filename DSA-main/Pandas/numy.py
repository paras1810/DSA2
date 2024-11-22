import numpy as np
array = np.array([[3,4,5],[6,7,8],[1,2,3]])
row, col = array.shape
for i in range(min(row, col)):
    array[i][i] = 1
print(array)