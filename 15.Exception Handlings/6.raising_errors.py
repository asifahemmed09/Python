def check_age(age):
    if age < 0:
        raise ValueError("Age can not be 0 or less than 0")
    elif age >= 150:
        raise ValueError("Age can not be more than 150")
    else:
        print(age)

try:
    check_age(222)
except Exception as e:
    print(type(e).__name__)
    print(e)
