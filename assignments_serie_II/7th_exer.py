"""
Considering a four dimensions array, how to get sum over the last two axis at once?
"""
import numpy as np

array = np.random.random((4, 5, 8, 2))
sum_array = np.sum(array, axis=(2, 3))
sum_array_2 = np.sum(array, axis=(0, 2))
# ...

print(sum_array, "\n\n", sum_array_2)
