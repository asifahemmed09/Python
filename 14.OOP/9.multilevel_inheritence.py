class Animal:
    def breath(self):
        print("breathing...")

class Mamal(Animal):
    def feed(self):
        print("feeding...")

class Dog(Mamal):
    def bark(self):
        print("barking...")

dog1 = Dog()
dog1.breath()
dog1.feed()
dog1.bark()
