
from typing import List
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv(
    "D:\Work\JIIT\Sem__5\Sem_5\OpenSourceLab\LabTest-1\Sales_Data.csv")
List



# create data
x = [1, 2, 3, 4, 5]
y = [3, 3, 3, 3, 3]

# plot lines
plt.plot(x, y, label="line 1", linestyle="-")
plt.plot(y, x, label="line 2", linestyle="--")
plt.plot(x, np.sin(x), label="curve 1", linestyle="-.")
plt.plot(x, np.cos(x), label="curve 2", linestyle=":")
plt.legend()
plt.show()
