marks = {
    "Science": 89,
    "Math": 99,
    "English": 78
}

sorted_marks = dict(sorted(marks.items(),key=lambda x: x[1]))
print(sorted_marks)
