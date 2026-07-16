"""
Write a function that print all the factors of a number entered by user.
"""

def get_all_factors(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")


num = int(input("Enter a number: "))
get_all_factors(num)
