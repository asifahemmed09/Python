"""
Take two numbers as input. Print the greater of the two. If they are
equal, print "Both are equal."
"""
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num1 > num2 :
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num2} is greater than {num1}")
else:
    print("Both the numbers are same")
