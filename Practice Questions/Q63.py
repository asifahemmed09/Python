"""
Top 3 Subjects by Marks

Given a dictionary of subjects and their marks, sort it by marks in descending
order. Then, print only the top 3 subjects with the highest marks.
"""

marks = {
    "English": 78,
    "Math": 89,
    "History": 98,
    "Economy": 88,
    "Science": 79,
    "Computer": 99
}

sorted_marks = sorted(marks.items(),key= lambda x: x[1],reverse=True)
top_three_subjects = dict(sorted_marks[0:3])
print(top_three_subjects)


