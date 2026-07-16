"""
Write a function called min_of_three that takes three numbers and returns
the smallest without using any built-in function.
"""
def min_of_three(a,b,c):
    if a > b and a > c:
       return a
    elif b > a and b > c:
        return b
    else:
        return c

print(min_of_three(22,565,23))
