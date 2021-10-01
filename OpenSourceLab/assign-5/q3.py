import numpy as np
from scipy import linalg

A = np.array([[4, 5], [3, 2]])
det = linalg.det(A)
print(det)


"""
-7.0
"""
