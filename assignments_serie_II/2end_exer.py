"""
Write a NumPy program to create a random 10x4 array and extract the first five rows of the array
and store them into a variable.
"""

import numpy as np
import random

arr = np.random.random((10, 4))
print(arr, "\n", type(arr))

new_arr = arr[0:5, :]
print(new_arr, new_arr.shape)

