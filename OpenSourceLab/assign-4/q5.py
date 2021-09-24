import numpy as np
a1 = np.array([0, 10, 20, 40, 60])
print("Arr 1: ", a1)
a2 = [0, 40]
print("Arr 2: ", a2)
print("Comparing arr 1 with arr 2")
print(np.in1d(a1, a2))

"""
[ True False False True False]

"""
