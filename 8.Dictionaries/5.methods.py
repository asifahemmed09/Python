marks = {
    "Science": 89,
    "Math": 99,
    "English": 78
}


for key in marks.keys():
    print(f"{key}: {marks[key]}")

for value in marks.values():
    print(value,end=" ")

print()

for key, value in marks.items():
    print(f"{key}: {value}")
