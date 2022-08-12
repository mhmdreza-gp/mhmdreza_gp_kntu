"""
an array so the values range exactly between 0 and 1?
array = np.random.randint(0, 1000, (1, 100))
"""

import numpy as np

array = np.random.randint(0, 1000, (1, 100))

new_array = array / 1000
print(new_array, "\n\n", new_array.min(), new_array.max())
