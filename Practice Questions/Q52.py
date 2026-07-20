"""
Given a list of marks, use list comprehension to create a new list that contains
only the marks that are above 75.
"""

marks = [55,66,78,77,98,88,99,81,50,84]
filter_marks = [mark for mark in marks if mark > 75]
print(filter_marks)
