"""
Write a program that takes a list and a target number. Use a loop to determine if
the target number exists in the list. Do not use the in operator.
"""

nums = [1,2,3,4,5]
n = 6

def is_exist(nums,n):
    for num in nums:
        if num == n:
            return f"{n} exists in nums list"
        else:
            continue
    else:
        return f"{n} does not exist in nums list"
print(is_exist(nums,n))
