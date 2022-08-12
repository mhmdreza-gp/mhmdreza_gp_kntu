"""
convert an nd array of arrays into a flat 1d array
"""

import numpy as np

arr = np.random.randint(0, 10, (3, 4, 5, 6))
size_arr = arr.size

reshaped_arr = arr.reshape(size_arr)
print(reshaped_arr, "\n", reshaped_arr.shape)
