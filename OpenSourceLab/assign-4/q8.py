import numpy as np

n_array = np.array([[50, 30], [30, 40]])

print("Matrix")
print(n_array)

det = np.linalg.det(n_array)
rank = np.linalg.matrix_rank(n_array)
trace = np.matrix.trace(n_array)

print("Rank")
print(int(rank))

print("Trace")
print(int(trace))

print("Determinant")
print(int(det))


"""
Matrix
[[50 30]
 [30 40]]
Rank
2
Trace
90
Determinant
1100
"""
