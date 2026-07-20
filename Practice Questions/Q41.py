"""
Given two lists of the same length, write Python code using a loop to create
a new list where each element is the sum of the corresponding elements from
both original lists.
"""
list_one = [1,2,3,4,5]
list_two = [6,7,8,9,10]
combined_list = []

for i in range(0,len(list_one)):
    total = list_one[i] + list_two[i]
    combined_list.append(total)


print(combined_list)
