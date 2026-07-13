"""
Take two numbers as input from the user. Print their sum, difference,
product, and remainder.
"""

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
remainder = num1 % num2

print(f"""
      number1 = {num1}
      number2 = {num2}
      sum = {sum}
      difference = {difference}
      product = {product}
      remainder = {remainder}
""")
