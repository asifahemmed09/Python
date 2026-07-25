class Flyer:
    def fly(self):
        print("flying...")

class Swimmer:
    def swim(self):
        print("swimming...")

class Duck(Flyer,Swimmer):
    def quack(self):
        print("quacking...")

duck = Duck()
duck.fly()
duck.swim()
duck.quack()
