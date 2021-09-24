import numpy as np

array = np.array((1, 2, 3))
print(array)

out_arr = np.column_stack((array))
print("Stacked Array ", out_arr)

"""
[1 2 3]
Stacked Array  [[1 2 3]]
"""
