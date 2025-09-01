
"""
    Write a short Python function that takes a positive integer n and returns
    the sum of the squares of all the positive integers smaller than n 
"""
def calc_sum(n):
    sq_sums = sum(i**2 for i in range(n))
    print(f"\nsum of Squares less than {n}: {sq_sums}\n")

calc_sum(5)