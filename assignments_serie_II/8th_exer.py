"""
Consider 2 points p0, p1 describing a line (2d) and a point p,
 how to compute distance from p to this line?
"""

import numpy as np


# def distance(p0, p1, p):


p0 = np.random.uniform(-10, 10, (1, 2))
p1 = np.random.uniform(-10, 10, (1, 2))
p = np.random.uniform(-10, 10, (1, 2))

print(distance(p0, p1, p))