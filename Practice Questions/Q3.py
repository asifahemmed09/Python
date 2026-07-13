"""
Take the user's age as input. Check and print whether they are eligible
to vote (age >= 18) and whether they are a senior citizen (age >= 60).
Print both results.
"""
age = int(input("Enter your age: "))

if age >= 18 and age>= 60:
    print("You are a senior citizen and eligible for vote")
elif age >= 18:
    print("You are eligible for vote")
else:
    print("You are not eligible for vote")
