"""
Take a number as input. Print whether it is even or odd using the %
operator and a comparison operator.
"""
number = int(input("Enter a number: "))

even_or_odd = "even" if number % 2 == 0 else "odd"

print(f"{number} is {even_or_odd}")
