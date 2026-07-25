class Point:
     def __init__(self, x, y):
        self.x = x
        self.y = y
     def __str__(self):
        return f"Point - {self.x,self.y}"
     def __eq__(self,other):
         return self.x == other.x and self.y == other.y
     def __add__(self,other):
         return self.x + other.x, self.y + other.y
     def __len__(self):
         return len((self.x,self.y))

p1 = Point(1,2)
p2 = Point(1,2)

print(p1)

print(p1 == p2)
print(p1 + p2)

print(len(p1))

