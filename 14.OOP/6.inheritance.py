class Vehicle:
    def __init__(self,brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting...")

class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} is driving...")

car1 = Car("Audi")
car1.start()
car1.drive()
