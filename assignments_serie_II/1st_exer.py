"""
Write a NumPy program to create a 5x5 array with random values
and find the minimum and maximum values.
"""

import numpy as np

arr = np.random.random((5, 5))
min_arr, max_arr = arr.max(), arr.min()
print(arr, "\n", min_arr, max_arr)
