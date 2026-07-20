"""
Given a list, remove all duplicate elements while preserving the original
order of the unique items.
"""
nums = [1, 5, 4, 5, 5, 6, 5, 4, 3, 5, 6, 7, 6, 7, 1, 1, 1]

unique_nums = []

for num in nums:
    if num not in unique_nums:
        unique_nums.append(num)

print(unique_nums)
