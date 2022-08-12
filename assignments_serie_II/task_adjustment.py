import numpy as np

# task -> ((A'PA)^-1)(A'PL)
A = np.array([[1, 2], [3, 5], [7, 6]])
P = np.diag([5, 5, 5])
L = np.array([7, 3, 2]).reshape((3, 1))

x = (np.linalg.inv(A.T @ P @ A)) @ (A.T @ P @ A)
print(x)

"""
or ;
j = A.T @ P @ A
x = np.linalg.inv(j) @ j
"""
