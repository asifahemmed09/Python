from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,height):
        self.length = length
        self.height = height
    def area(self):
        print(self.length * self.height)

rect = Rectangle(2,2)
rect.area()


