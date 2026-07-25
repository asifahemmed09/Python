class Student:
    def __init__(self,name: str,age: int,marks: list[int]):
        self.name = name
        self.age = age
        self.marks = marks

    def total(self)-> int:
        return sum(self.marks)
    def average(self)-> int:
        return sum(self.marks) // len(self.marks)
    def grade(self):
        avg = self.average()
        if avg > 80:
            print("A")
        elif avg > 60 and avg < 80:
            print("B")
        else:
            print("C")


john = Student("John Doe", 24, [76,88,94])

print(john.total())
print(john.average())
john.grade()
