import numpy as np
from scipy import linalg

A = np.array([[4, 5], [3, 2]])
eval, evector = linalg.eig(A)


print(eval)
print(evector)


"""
[ 7.+0.j -1.+0.j]

[[ 0.85749293 -0.70710678]
 [ 0.51449576  0.70710678]]

"""
