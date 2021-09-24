import numpy as np
array1 = np.array([0, 10, 20, 40, 60, 80])
print(array1)
array2 = [10, 30, 40, 50, 70]
print(array2)
print("unique Sorted araays")
print(np.setxor1d(array1, array2))

"""
[ 0 10 20 40 60 80]
[10, 30, 40, 50, 70]

unique Sorted araays
[ 0 20 30 50 60 70 80]

"""
