marks = [55,87,99,45,67,69]

# built-in functions
n = len(marks)
print(f"Length of marks is {n}")

maximum = max(marks)
print(f"Maximum element in list is {maximum}")

minimum = min(marks)
print(f"Minimum element in list is {minimum}")

sorted_marks = sorted(marks)
print(f"Sorted marks : {sorted_marks}")

sorted_marks_desc = sorted(marks,reverse=True)
print(f"Sorted marks descending: {sorted_marks_desc}")

