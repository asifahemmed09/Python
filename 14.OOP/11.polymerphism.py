class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length):
        self.length = length
    def area(self):
            return self.length * self.length

class Rectangular(Shape):
    def __init__(self,length,width):
            self.length = length
            self.width = width
    def area(self):
                return self.length * self.width

class Circle(Shape):
     def __init__(self,radius):
                 self.radius = radius
     def area(self):
                return  3.14 * self.radius ** 2

shapes = [Square(2),Rectangular(2,4),Circle(0.5)]

for shape in shapes:
       area = shape.area()
       print(area)
