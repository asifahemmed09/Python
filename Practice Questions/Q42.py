"""
Write a program that takes a list of numbers and, using a loop, determines
whether it is sorted in ascending order. Print True if it is sorted,
and False otherwise.
"""
nums = [1,2,3,4,5]

for i in range(1,len(nums)):
    if not nums[i]  > nums[i - 1]:
        print("False")
        break
else:
    print("True")
