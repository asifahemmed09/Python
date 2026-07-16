"""
Write a function called find_max that takes three numbers as
parameters and prints the largest one.
"""
def find_max(a,b,c):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)


find_max(55,33,66)
