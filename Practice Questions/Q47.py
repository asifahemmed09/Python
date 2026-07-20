"""
Separate a list of integers into two distinct lists: one containing all the
even numbers and the other containing all the odd numbers.
"""

nums = [1,2,3,4,5,6,7,8,9,10]
odd_nums = []
even_nums = []

for num in nums:
    if num % 2 == 0:
        even_nums.append(num)
    else:
        odd_nums.append(num)

print(odd_nums)
print(even_nums)
