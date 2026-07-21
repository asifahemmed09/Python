"""
Student Marks Analysis

Design a dictionary where each key is a student's name and the corresponding
value is a list of their marks in 3 different subjects. Calculate and print
the total marks and average marks for each student.
"""

marks = {
    "Smith": [66,75,89],
    "John": [76,75,99],
    "Roger": [87,85,89]
}

for key,value in marks.items():
    total = 0
    for i in value:
        total+= i
    average = total // len(value)
    print(f"{key}'s total mark is {total} and average is {average}")

