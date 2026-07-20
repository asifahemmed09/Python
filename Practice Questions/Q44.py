"""
Reverse a list without using the .reverse() method or list slicing ([::-1]).
"""

nums = [1,2,3,4,5]
reversed_nums = []

for i in range(len(nums) - 1, -1, -1):
    reversed_nums.append(nums[i])
print(reversed_nums)


