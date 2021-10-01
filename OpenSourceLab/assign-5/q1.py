import numpy as np
from scipy import io as sci

array = np.ones((4, 4))
sci.savemat('example.mat', {'ar': array})
data = sci.loadmat('example.mat', struct_as_record=True)
print(data['ar'])


"""
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]

"""
