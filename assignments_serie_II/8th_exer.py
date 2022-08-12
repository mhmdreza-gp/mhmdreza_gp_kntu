"""
Consider 2 points p0, p1 describing a line (2d) and a point p,
 how to compute distance from p to this line?
"""

import numpy as np
from numpy.linalg import norm


def distance_calculator(a, b, c):
    d = np.cross(b - a, a - c) / norm(b - a)
    return np.absolute(d)


p0 = np.random.uniform(-10, 10, (1, 2))
p1 = np.random.uniform(-10, 10, (1, 2))
p = np.random.uniform(-10, 10, (1, 2))

print(distance_calculator(p0, p1, p))

"""
actually, I could not write this code all by my self & it comes from search in google.
here we have some tips about written code:

<np.cross> : returns the z-coordinate of the cross product only for 2D vectors.
The cross product of a and b in  is a vector perpendicular to both a and b. If a and b are arrays of vectors,
the vectors are defined by the last axis of a and b by default,
and these axes can have dimensions 2 or 3. 

when <np.linalg.norm()> is called on an array-like input without any additional arguments,
the default behavior is to compute the L2 norm on a flattened view of the array.
This is the square root of the sum of squared elements 
and can be interpreted as the length of the vector in Euclidean space.
"""