def change_list(x):
    x.append(10)
    x[0] = 11
    print(f"List inside function: {nums}")

nums = [1,2,3,4,5]
change_list(nums)
print(f"List outside function: {nums}")
