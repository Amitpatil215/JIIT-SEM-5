import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt

inp = list(map(str, input().strip().split()))
inp_new = [ele+"0"*(7-len(ele)) if ele.isnumeric() else ele for ele in inp]

print("After operation string is\n", inp_new)

hist = []
for ele in range(len(inp)):
    res = abs(len(inp[ele]) - len(inp_new[ele]))
    if(res > 0):
        hist.append(res)

plt.figure(figsize=(12, 6), dpi=80)
plt.hist(hist, bins=10)
ax = plt.gca()
ax.set_title('Histogram')
ax.set_xlabel('Word Length')
ax.set_ylabel('Count')
plt.show()
