"""
Ask a number from the user, and count all the factors.
"""

num = int(input("Enter a number: "))

i = 1
count = 0

while i <= num:
    if num % i == 0:
        count += 1
    i += 1

print(count)
