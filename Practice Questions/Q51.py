"""
Using list comprehension, create a list of squares of all odd numbers from 1 to 20.
"""
odd_squares = [x * x for x in range(1,21) if not x % 2 == 0]
print(odd_squares)
