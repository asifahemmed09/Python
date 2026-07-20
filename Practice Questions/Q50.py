"""
Write a Python script that iterates through a list of integers and replaces every
negative number found in the list with the value 0.
"""
nums = [1,-3,7,-4,8,-5,6]

for i in range(0,len(nums)):
    if nums[i] < 0:
        nums[i] = 0

print(nums)
