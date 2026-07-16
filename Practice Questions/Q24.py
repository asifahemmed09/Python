"""
Write a function that ask a number from user and prints if that
number is odd or even.
"""

num = int(input("Enter a number: "))

def odd_even(num):
    if num % 2 == 0:
        print(f"{num} is even number")
    else:
        print(f"{num} is odd number")

odd_even(num)
