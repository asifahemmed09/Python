"""
Given a list of numbers (which may contain duplicates), write a Python script
that takes an integer as input from the user and removes all occurrences of that
integer from the list.
"""

nums = [2,4,5,5,44,7,8,6,7,55,44,5,3]
x = int(input("Enter a number: "))

while x in nums:
    nums.remove(x)



print(nums)
