try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Can not divide by zero")
except ValueError:
    print("Invalid Input")
except:
    print("Some error occured")
