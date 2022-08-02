"""
Write a Python program to sum of two given integers.
However, if the sum is between 15 to 20 it will return 20.
"""

a = int(input("1st number: "))
b = int(input("2end number: "))

lst = [a, b]

sum_ = lambda x, y: x + y

res = [20 if 15 < sum_(a, b) < 20 else sum_(a, b)]
print(res)
