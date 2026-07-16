# keyword arguments
def calculate_marks(math,english,history = 0):
    total = math + english + history
    return f"Total Marks: {total}"

print(calculate_marks(english=92,math=78))
