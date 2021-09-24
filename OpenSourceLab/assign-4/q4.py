import numpy as np
Z = np.ones((3, 3))
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
print(Z)


"""
[[0. 0. 0. 0. 0.]
 [0. 1. 1. 1. 0.]
 [0. 1. 1. 1. 0.]
 [0. 1. 1. 1. 0.]
 [0. 0. 0. 0. 0.]]
"""
