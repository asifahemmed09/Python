my_list = [1,2,3,4]
copy_list = my_list.copy()

print(id(my_list))
print(id(copy_list))

copy_list.append(10)

print(my_list)
print(copy_list)

