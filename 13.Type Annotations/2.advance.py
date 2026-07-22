def max_in_list(nums: list[int]) -> int:
    max_num = max(nums)
    return max_num

max_num = max_in_list([1,2,3,4,5])
print(max_num)

def get_details(person: dict[str,str | int | bool]) -> None:
    print(f"{person["name"]} is {person["age"]} years old and is a {"student" if person["is_student"] else "not student"}")

get_details({"name":"Asif","age":29,"is_student":True})

