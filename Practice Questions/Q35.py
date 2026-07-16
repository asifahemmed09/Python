"""
Write a function fizzbuzz(n) that takes a single number and prints "Fizz"
if it's divisible by 3,"Buzz" if it's divisible by 5,"FizzBuzz" if it's divisible by both,
otherwise print the number itself.
"""

def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 5 == 0:
        print("Fizz")
    elif n % 3 == 0:
        print("Buzz")
    else:
        print(n)


fizz_buzz(9)
fizz_buzz(10)
fizz_buzz(15)
fizz_buzz(17)
