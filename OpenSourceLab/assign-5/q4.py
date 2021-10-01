import numpy as np
from scipy import linalg

A = np.array([[4, 5], [3, 2]])
inverse = linalg.inv(A)
print(A)
print(inverse)

"""
[[4 5]
 [3 2]]

[[-0.28571429  0.71428571]
 [ 0.42857143 -0.57142857]]

"""
