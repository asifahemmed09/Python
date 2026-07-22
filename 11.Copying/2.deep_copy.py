import copy

my_list = [1,2,[1,2],3,4]
copy_list = copy.deepcopy(my_list)

print(id(my_list))
print(id(copy_list))

copy_list.append(10)
copy_list[2][0] = 10

print(my_list)
print(copy_list)
