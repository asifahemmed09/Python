nums = [1,2,3,4,5]

# while loop
n = len(nums)
count = 0
while count < n:
    print(nums[count], end=" ")
    count += 1

print("\n")

# for loop
for i in range(0,n):
    print(nums[i],end=" ")

print("\n")

for num in nums:
    print(num, end=" ")

print("\n")

# enumerate
for index,value in enumerate(nums):
    print(f"Index-{index}, Value-{value}")
