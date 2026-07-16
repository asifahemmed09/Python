# local variable
def add(a,b):
    total = a + b # local variable
    print(total)

add(1,2)

# global variable


name = "John Doe" # global variable

def greet():
    global name
    name = "Sam Smith"
    print(f"Hello {name}")

greet()
print(name)
