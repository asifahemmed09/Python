try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(result)
except Exception as e:
    print(type(e).__name__)
    print(e)

