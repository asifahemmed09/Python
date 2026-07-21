my_set = {1,2,3,4,5,6,}
print(my_set)

# adding a element
my_set.add(7)
print(my_set)

# updating set
my_set.update([8])
print(my_set)

# removing a element
my_set.remove(8) # if does not exist will give an error
print(my_set)

my_set.discard(7) # if does not exist will not give an error
print(my_set)

poped = my_set.pop()
print(poped)
print(my_set)




