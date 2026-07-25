class Vehicle:
    def __init__(self,brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self,brand,engine):
        super().__init__(brand)
        self.engine = engine

car1 = Car("Audi","Fuel")
print(car1.brand)
print(car1.engine)
