"""
A student scored marks in 3 subjects. Take all three as input,
calculate the total and average, and print both using an f-string.
"""

physics = int(input("Enter your Physics marks: "))
chemistry = int(input("Enter your Chemistry marks: "))
math = int(input("Enter your Math marks: "))

print(f"Your total mark is {physics + chemistry + math} and average is {(physics + chemistry + math)/ 3:.2f}")
