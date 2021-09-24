import numpy as np

def characterfrequency(str):

    n = len(str)

    frequency = np.zeros(26, dtype=np.int64)

    for i in range(0, n):
        frequency[ord(str[i]) - ord('a')] += 1

    for i in range(0, n):

        if (frequency[ord(str[i]) - ord('a')] != 0):

            print(str[i], frequency[ord(str[i]) - ord('a')],
                  end=" ")

        frequency[ord(str[i]) - ord('a')] = 0



strr = "amit"
characterfrequency(strr)

"""
a 1 m 1 i 1 t 1
"""
