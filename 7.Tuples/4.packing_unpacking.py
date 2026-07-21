def get_min_max(nums):
    min_num = min(nums)
    max_num = max(nums)

    return min_num, max_num

min_num, max_num = get_min_max([22,44,64,6,333,687,88,53,211,1])

print(min_num,max_num)
