"""
Given a list of numbers, write Python code using a loop to find and print the
largest element. Do not use the built-in max() function.
"""
nums = [2,55,32,7,99,134,38,3]
largest_element = 0
for num in nums:
    if num > largest_element:
        largest_element = num

print(f"Largest element in the list is {largest_element}")
