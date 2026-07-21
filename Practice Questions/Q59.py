"""
Subject Performance Analysis

Given a dictionary of marks for different subjects, loop over its values() to
calculate and print the total marks and the average mark obtained.
"""

marks = {
    "Science": 89,
    "Math": 99,
    "English": 78
}

total = 0
count = 0

for value in marks.values():
    total += value
    count += 1

average = total // count

print(f"Total Mark: {total} , Average Mark:{average}")
