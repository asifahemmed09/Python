"""
Populate a dictionary with six student names and their corresponding marks.
Loop through it and print the names of all students who achieved a score above 75.
"""

marks = {
    "Jack": 89,
    "William": 66,
    "Smith": 78,
    "Binny": 99,
    "John": 54,
    "Robert": 80
}

for key,value in marks.items():
    if value > 75:
        print(key)
