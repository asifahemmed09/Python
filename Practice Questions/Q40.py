"""
Given a list of numbers, use a loop to calculate and print their average.
You can use len() to get the count of elements, but avoid using
sum() for the total.
"""
nums = [1,2,3,4,5]
total = 0
n = len(nums)

for num in nums:
    total += num

average = total // n
print(f"Average: {average}")
