"""
Given two lists, merge them into a single new list without modifying the originals.
"""
num1 = [1, 2, 3]
num2 = [65, 32, 11]
merged_num = []

for num in num1:
    merged_num.append(num)

for num in num2:
    merged_num.append(num)

print(merged_num)
