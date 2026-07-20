fruits = ["apple","banana","watermelon","kiwi","avocado"]

# adding an elements to list at the last index
fruits.append("Lichi")
print(fruits)

# adding an elements to list at a specific index
fruits.insert(2,"jackfruit")
print(fruits)

# removing an elements from the last index
last_fruit = fruits.pop()
print(last_fruit)
print(fruits)

# removing an elements from at a specific index
poped_fruit = fruits.pop(2)
print(poped_fruit)
print(fruits)

# removing a specific element
fruits.remove("watermelon")
print(fruits)

nums = [1,3,5,2,4]

# sorting a list
nums.sort() #ascending
print(nums)

nums.sort(reverse=True) #descending
print(nums)

# reversing a list
nums.reverse()
print(nums)

# finding a index of an element in a list
index_of_one = nums.index(1)
print(index_of_one)

# count of occurence of an element in a list
nums = [1,2,2,3,3,3,4,4,4,4]
print(nums.count(3))


