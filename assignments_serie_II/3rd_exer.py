"""
Write a NumPy program to create random vector of size 15 and replace the maximum value by -1.
"""

import numpy as np

vector = np.random.randint(0, 20, (1, 15))
print(vector, vector.shape, "  max = ", vector.max())

max_element = np.where(vector == vector.max())
vector[max_element] = -1
print(max_element, "\n", vector)

"""
also we can get indexes separately like : 

rows, cols = np.where(vector == vector.max())
print(rows, cols)

"""
